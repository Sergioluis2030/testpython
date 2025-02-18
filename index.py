import httpx
import json

def lambda_handler(event, context):
    url = "https://jsh4moljr3.execute-api.us-east-2.amazonaws.com/dev/test"
    
    # Extraer datos del evento o usar un payload predeterminado
    payload = event.get("body")
    if isinstance(payload, str):
        payload = json.loads(payload)

    try:
        # Realizar la petición POST
        response = httpx.post(url, json=payload, timeout=10)

        # Verificar si la petición fue exitosa
        if response.status_code == 201:
            return {
                "statusCode": 201,
                "body": json.dumps({
                    "message": "✅ Petición exitosa!",
                    "response": response.json()
                })
            }
        else:
            return {
                "statusCode": response.status_code,
                "body": json.dumps({
                    "message": f"⚠️ Error: {response.status_code}",
                    "details": response.text
                })
            }

    except httpx.RequestError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "❌ Error de conexión",
                "error": str(e)
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "⚠️ Error inesperado",
                "error": str(e)
            })
        }
