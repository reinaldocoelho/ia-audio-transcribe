# enTranscribe

API para transcrição de audio para uso de forma simples pelo enContact, para obter a transcrição de audios.

A transcrição aceita arquivos: wav, ogg ou opus

## Como funciona

1. Baixe um modelo de linguagem que deseja usar na transcrição, utilizando o link: <https://alphacephei.com/vosk/models>
2. Ao subir o container, monte o volume '/app/model' apontando para o modelo que você baixou
    * Ex: VOLUME: $(pwd)/model/vosk-model-small-pt-0.3:/app/model
3. Efetue a chamada da API conforme os exemplos de uso, enviando seu arquivo como conteúdo da chamada.

## Exemplo de uso

Para processar arquivos .opus:

```bash
curl -X POST "http://localhost:8000/transcribe/" \
  -H  "accept: application/json" \
  -H  "Content-Type: multipart/form-data" \
  -F "file=@teste.opus"
```

Para processar arquivos .wave: 

```bash
curl -X POST "http://localhost:8000/transcribe/" \
  -H  "accept: application/json" \
  -H  "Content-Type: multipart/form-data" \
  -F "file=@teste.wav"
```

## Referências

* https://alphacephei.com/vosk/models
* https://chatgpt.com/share/67e47e5e-f09c-800a-9473-7b632bc9b783


## Mais informações sobre o projeto

Estrutura do projeto:

```
vosk-api/
├── app/
│   ├── main.py
│   └── model/
│       └── (aqui vai o modelo do Vosk baixado)
├── Dockerfile
├── requirements.txt
```
