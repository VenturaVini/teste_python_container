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
import requests
from time import sleep
from services.telegram import enviar_mensagem

def main():
    print("🔁 Iniciando teste Python...")
    
    try:
        response = requests.get("https://httpbin.org/get", timeout=10)
        print("✅ Status Code:", response.status_code)

        try:
            dados = response.json()
            print("📦 Dados:", dados)
        except requests.exceptions.JSONDecodeError:
            print("❌ Erro ao decodificar JSON.")
            print("📄 Conteúdo bruto:", response.text)
            enviar_mensagem('Telegram Funcionando!!')
            return

        sleep(15)
        print("📦 Reutilizando Dados:", dados)
        enviar_mensagem('Telegram Funcionando!!')
        enviar_mensagem('✅ Telegram Funcionando!!')

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
        enviar_mensagem('❌ Falha ao acessar a API.')

if __name__ == "__main__":
    main()
