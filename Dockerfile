# Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de requisitos para o container
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do aplicativo para o container
COPY . .

# Exponha a porta que o Flask usará
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["python", "todo_project/run.py"]