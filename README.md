# enTranscribe

API para transcrição de audio para uso de forma simples pelo enContact, para obter a transcrição de audios.

## Exemplo de uso

Para processar arquivos .opus:

```bash
curl -X POST "http://localhost:8000/transcribe/" \
  -H  "accept: application/json" \
  -H  "Content-Type: multipart/form-data" \
  -F "file=@audio-foca-teste.opus"
```

Para processar arquivos .wave: 

```bash
curl -X POST "http://localhost:8000/transcribe/" \
  -H  "accept: application/json" \
  -H  "Content-Type: multipart/form-data" \
  -F "file=@audio-foca-teste.opus"
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
