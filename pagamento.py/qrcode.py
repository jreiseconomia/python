import requests
import json

# Substitua pela sua API Key do OpenPix
API_KEY = "SUA_API_KEY"

def gerar_qr_code(valor, nome_cliente):
    url = "https://api.openpix.com.br/api/v1/charge"

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "correlationID": "rifa-" + nome_cliente,
        "value": int(valor * 100),  # Valor em centavos
        "comment": "Rifa Online",
        "customer": {
            "name": nome_cliente
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()

    return data["brCode"], data["qrCodeImage"]

# Exemplo de uso:
br_code, qr_image = gerar_qr_code(10.00, "João Silva")
print(f"BR Code: {br_code}")
print(f"QR Code Image: {qr_image}")
