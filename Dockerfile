# Dockerfile
FROM python:3.10-slim

# Diretório de trabalho
WORKDIR /code

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Porta que o Uvicorn vai usar
EXPOSE 8000

# Comando default (usado no docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
