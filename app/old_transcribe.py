#### ESTE FOI O SCRIPT V1.0, E NAO ESTA EM USO

from vosk import Model, KaldiRecognizer
from pydub import AudioSegment  # Para conversão de formatos de áudio
import wave
import os
import shutil

# Carregar o modelo do Vosk
model_path = "/app/model"
model = Model(model_path)


input_file = "/app/audio/audio-foca-teste.wav"
output_file = "/app/audio/to_extract.wav"

if input_file.endswith(".wav"):
    shutil.copyfile(input_file, output_file)
else:
    print("Aqui deveria converter o que tiver pra Wav")
    #### BLOCO PARA CONVERTER O AUDIO PARA WAVE
    ## Definir o nome do arquivo de entrada e saída
    #input_file = "/app/audio/audio-foca-teste.opus"
    #output_file = "/app/audio/temp_audio.wav"

    ## Converter .opus para .wav usando Pydub e FFmpeg
    #print("Convertendo arquivo .opus para .wav...")
    #audio = AudioSegment.from_file(input_file, format="opus")
    #audio.export(output_file, format="wav")
    #### FIM CONVERSAO


# Abrir o arquivo WAV convertido
wf = wave.open(output_file, "rb")
rec = KaldiRecognizer(model, wf.getframerate())

# Processar e transcrever o áudio
print("Iniciando transcrição do áudio...")
result = "["
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result += rec.Result()
        print(rec.Result())

result += rec.FinalResult() + "]"
print(result)

file = open('/app/output/result.json', 'w')
file.write(result)
file.close()

# Remover o arquivo temporário .wav após o processamento
os.remove(output_file)
