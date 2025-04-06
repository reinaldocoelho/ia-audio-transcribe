#!/bin/bash

docker build -t vosk-api .
docker run -p 8000:8000 -v ./model/vosk-model-small-pt-0.3:/app/model vosk-api
# ./model/vosk-model-small-pt-0.3:/app/model

# docker-compose build
# docker-compose up

## Para inspecionar o container:
## docker exec -it vosk-transcriber-1 bash
