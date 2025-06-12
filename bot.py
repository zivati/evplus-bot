
import time
import requests
from flask import Flask
import os

# Variáveis do Telegram
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Inicializa app Flask
app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return "OK", 200

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Erro ao enviar para o Telegram:", e)

def analisar_e_alertar():
    # Exemplo fixo de mensagem EV+ (simulação)
    mensagem = (
        "📊 [ALERTA – MLB]\n\n"
        "⚾️ Yankees x Red Sox\n"
        "🧾 UNDER 9.5 Total de Corridas\n"
        "📈 Modelos: 8.1 corridas\n"
        "💸 EV+: +7.4%\n"
        "🔐 Score: 8.3 / 10\n\n"
        "🔍 Motivos:\n- Clima: vento contrário\n- Lineup confirmado\n- Steam move detectado\n\n"
        "🕒 Jogo: 20h10"
    )
    enviar_telegram(mensagem)

if __name__ == "__main__":
    enviar_telegram("🟢 Bot iniciado com sucesso — tudo operacional.")
    from threading import Thread
    Thread(target=lambda: app.run(host="0.0.0.0", port=10000)).start()
    while True:
        analisar_e_alertar()
        time.sleep(300)
