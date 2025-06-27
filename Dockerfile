FROM python:3.10-slim

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos
#COPY requirements.txt .
#COPY main.py .
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão ao rodar o container
CMD ["python", "main.py"]
