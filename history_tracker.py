
import json
import os
from datetime import datetime

HIST_DIR = "history"
os.makedirs(HIST_DIR, exist_ok=True)

def salvar_historico_jogo(dados: dict, liga: str):
    dia = datetime.now().strftime("%Y-%m-%d")
    filename = f"{HIST_DIR}/{liga}_{dia}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            historico = json.load(f)
    else:
        historico = []

    historico.append(dados)
    with open(filename, "w") as f:
        json.dump(historico, f, indent=2)
