from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from vosk import Model, KaldiRecognizer
import subprocess
import wave
import os
import uuid
import shutil

app = FastAPI()

# Carregar o modelo do Vosk
MODEL_PATH = "/app/model"
model = Model(MODEL_PATH)

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    # if not file.filename.endswith((".wav", ".opus", ".mp3", ".flac")):
    #     raise HTTPException(status_code=400, detail="Formato de áudio não suportado")
    if not file.filename.endswith((".wav", ".opus", ".ogg")):
        raise HTTPException(status_code=400, detail="Formato de áudio não suportado")

    # Nome temporário para os arquivos
    input_ext = file.filename.split(".")[-1]
    temp_input = f"/tmp/{uuid.uuid4()}.{input_ext}"
    temp_wav = f"/tmp/{uuid.uuid4()}.wav"

    # Salvar o arquivo de entrada (binario recebido como arquivo local)
    with open(temp_input, "wb") as f:
        f.write(await file.read())

    # Inicia o processamento
    try:
        # Garante que exista o arquivo .wav para transcrever
        if file.filename.endswith((".wav")):
            shutil.copyfile(temp_input, temp_wav)
        elif file.filename.endswith((".opus")) or file.filename.endswith((".ogg")):
            print(f"Iniciando a conversao do arquivo {file.filename} para .wav")
            subprocess.run(["ffmpeg", "-i", temp_input, "-ar", "16000", "-ac", "1", temp_wav], check=True)
            print("Conversao concluida, seguindo para transcricao")
        else:
            return JSONResponse(status_code=500, content={"error": "Tipo de arquivo não suportado"})

        # Realiza a transcrição
        with wave.open(temp_wav, "rb") as wf:
            rec = KaldiRecognizer(model, wf.getframerate())
            results = []
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    results.append(rec.Result())

            results.append(rec.FinalResult())

        # Limpeza
        os.remove(temp_input)
        os.remove(temp_wav)

        return JSONResponse(content={"results": results})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})