
import json
import os
from collections import defaultdict
from datetime import datetime

HIST_DIR = "history"

def gerar_painel_resumo():
    resumo = defaultdict(lambda: {"spread": 0, "total": 0, "ml": 0})
    for file in os.listdir(HIST_DIR):
        if file.endswith(".json"):
            parts = file.split("_")
            liga = parts[0]
            with open(os.path.join(HIST_DIR, file), "r") as f:
                jogos = json.load(f)
                for j in jogos:
                    tipo = j.get("tipo", "")
                    if tipo in resumo[liga]:
                        resumo[liga][tipo] += 1

    painel = {
        "data_geracao": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "resumo": resumo
    }
    with open("painel_estatistico.json", "w") as f:
        json.dump(painel, f, indent=2)
