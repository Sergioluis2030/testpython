import httpx

url = "https://jsh4moljr3.execute-api.us-east-2.amazonaws.com/dev/test"
payload = {
    "title": "Prueba con httpx",
    "body": "Este es un mensaje de prueba usando httpx",
    "userId": 1
}

try:
    # Realizar la petición POST
    response = httpx.post(url, json=payload, timeout=10)
    
    # Verificar si la petición fue exitosa
    if response.status_code == 201:
        print("✅ Petición exitosa!")
        print(response.json())
    else:
        print(f"⚠️ Error: {response.status_code}")
        print(response.text)

except httpx.RequestError as e:
    print(f"❌ Error de conexión: {e}")
except Exception as e:
    print(f"⚠️ Error inesperado: {e}")
