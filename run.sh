#!/bin/bash

# Compila o container para a execução
docker build -t vosk-api .
# Aqui deve mapear a porta onde vai executar a API e apontar o mapeamento para o Modelo de IA para Transpilar
docker run -p 8000:8000 -v $(pwd)/model/vosk-model-small-pt-0.3:/app/model vosk-api
# ./model/vosk-model-small-pt-0.3:/app/model

## Execução do compose
# docker-compose build
# docker-compose up

## Para inspecionar o container:
## docker exec -it vosk-api bash
