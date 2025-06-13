
import requests
from telegram_bot.message_formatter import gerar_analise_dia
from main import orquestrar_analise

TELEGRAM_TOKEN = "7523685081:AAFIngESWWNZh5IqWD6j46X63I_oArpGNQE"
CHAT_ID = "896985205"

def enviar_telegram(texto: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": texto,
        "parse_mode": "HTML"
    }
    r = requests.post(url, json=payload)
    r.raise_for_status()
    return r.json()

def enviar_analise_completa(league: str):
    jogos = orquestrar_analise(league)
    mensagem = gerar_analise_dia(jogos)
    return enviar_telegram(mensagem)
