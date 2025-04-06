# # Use uma imagem oficial do Python como base
FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# # Use uma imagem oficial do Python como base
# FROM python:3.10-slim

# # Instalar dependências do sistema e FFmpeg
# RUN apt-get update && apt-get install -y ffmpeg libsndfile1 wget

# # Definir diretório de trabalho e copiar arquivos
# WORKDIR /app
# COPY requirements.txt .
# COPY transcribe.py .

# # Instalar dependências Python
# RUN pip install --no-cache-dir -r requirements.txt

# # Comando padrão do container
# CMD ["python", "transcribe.py"]
