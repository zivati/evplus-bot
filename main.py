
from flask import Flask, jsonify, send_file
from telegram_bot.bot import enviar_analise_completa
from utils.painel import gerar_painel_resumo
import os
import json

app = Flask(__name__)

@app.route("/healthz", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route("/send-daily", methods=["GET"])
def send_daily_analysis():
    enviar_analise_completa("nba")
    return jsonify({"status": "ok"}), 200

@app.route("/painel", methods=["GET"])
def painel_view():
    gerar_painel_resumo()
    with open("painel_estatistico.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/painel-grafico", methods=["GET"])
def painel_grafico():
    from utils.painel_grafico import gerar_grafico_painel
    path = gerar_grafico_painel()
    return send_file(path, mimetype='image/png')

@app.route("/painel-relatorio", methods=["GET"])
def painel_pdf():
    from utils.painel_pdf import gerar_relatorio_pdf
    path = gerar_relatorio_pdf()
    return send_file(path, mimetype='application/pdf')
