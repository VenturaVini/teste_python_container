import requests
from time import sleep

def main():
    print("🔁 Iniciando teste Python...")
    response = requests.get("https://httpbin.org/get")
    print("✅ Status Code:", response.status_code)
    print("📦 Dados:", response.json())
    sleep(15)
    print("📦 Dados:", response.json())

if __name__ == "__main__":
    main()
