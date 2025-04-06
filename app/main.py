from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from vosk import Model, KaldiRecognizer
# from pydub import AudioSegment
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
    if not file.filename.endswith((".wav")):
        raise HTTPException(status_code=400, detail="Formato de áudio não suportado")

    # Nome temporário para os arquivos
    input_ext = file.filename.split(".")[-1]
    temp_input = f"/tmp/{uuid.uuid4()}.{input_ext}"
    temp_wav = f"/tmp/{uuid.uuid4()}.wav"

    # Salvar o arquivo de entrada
    with open(temp_input, "wb") as f:
        f.write(await file.read())

    try:
        if file.filename.endswith((".wav")):
            shutil.copyfile(temp_input, temp_wav)
        ## Caso contrario tenta converter o imput para Wave
        # else
        # # Converter para WAV com pydub
        # audio = AudioSegment.from_file(temp_input)
        # audio.export(temp_wav, format="wav")
        # # Converte para wav usando ffmpeg
        # subprocess.run(["ffmpeg", "-i", tmp.name, "-ar", "16000", "-ac", "1", wav_path], check=True)


        # Abrir WAV com wave
        wf = wave.open(temp_wav, "rb")
        rec = KaldiRecognizer(model, wf.getframerate())

        results = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                res = rec.Result()
                results.append(res)
        results.append(rec.FinalResult())

        # Limpeza
        os.remove(temp_input)
        os.remove(temp_wav)

        return JSONResponse(content={"results": results})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
