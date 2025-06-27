import requests

def main():
    print("🔁 Iniciando teste Python...")
    response = requests.get("https://httpbin.org/get")
    print("✅ Status Code:", response.status_code)
    print("📦 Dados:", response.json())

if __name__ == "__main__":
    main()
