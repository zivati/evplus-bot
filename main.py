
from flask import Flask, jsonify
from telegram_bot.bot import enviar_analise_completa

app = Flask(__name__)

@app.route("/healthz", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route("/send-daily", methods=["GET"])
def send_daily_analysis():
    try:
        enviar_analise_completa("nba")
        return jsonify({"status": "enviado"}), 200
    except Exception as e:
        return jsonify({"status": "erro", "detalhe": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
