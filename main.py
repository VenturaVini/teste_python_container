import requests
from time import sleep
from services.telegram import enviar_mensagem

def main():
    print("🔁 Iniciando teste Python...")
    response = requests.get("https://httpbin.org/get")
    print("✅ Status Code:", response.status_code)
    print("📦 Dados:", response.json())
    sleep(15)
    print("📦 Dados:", response.json())
    enviar_mensagem('Telegram Funcionando!!')


if __name__ == "__main__":
    main()
