import requests

# ================================
# CONFIGURACIÓN
# ================================

# Pega aquí tu token de BotFather
BOT_TOKEN = "8177223756:AAEgF4dYB-TUdIO_B9ReKSaVwF3CHzIYTe0"

# Tu Telegram User ID (ya lo sacamos de getUpdates)
CHAT_IDS = [130531908]
#CHAT_IDS = [130531908, 5311773263, 5424918901, 5682381467]
# Mensaje que quieres enviar
TEXT = "¡Hola Ulises! 🚀 Tu bot ya está enviando mensajes."

def send_message(chat_id, text):
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    return response.json()

def send_to_all(text):
    results = []
    for chat_id in CHAT_IDS:
        r = send_message(chat_id, text)
        results.append({"chat_id": chat_id, "result": r})
    return results


