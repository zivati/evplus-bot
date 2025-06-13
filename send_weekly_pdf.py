
import schedule
import time
from telegram_bot.bot import enviar_telegram
from utils.painel_pdf import gerar_relatorio_pdf

def enviar_pdf_telegram():
    path = gerar_relatorio_pdf()
    with open(path, 'rb') as f:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument",
            data={"chat_id": CHAT_ID},
            files={"document": f}
        )

# Agendar para segunda-feira às 11h
schedule.every().monday.at("11:00").do(enviar_pdf_telegram)

def loop_agendamento():
    while True:
        schedule.run_pending()
        time.sleep(30)
