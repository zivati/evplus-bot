
import json
import matplotlib.pyplot as plt

def gerar_grafico_painel(path_json='painel_estatistico.json'):
    with open(path_json, 'r') as f:
        data = json.load(f)

    resumo = data['resumo']
    fig, ax = plt.subplots(figsize=(8, 5))

    for liga, valores in resumo.items():
        tipos = list(valores.keys())
        valores_plot = list(valores.values())
        ax.bar([f"{liga.upper()}-{t}" for t in tipos], valores_plot)

    ax.set_title("Volume de EV+ Detectados por Liga e Tipo de Linha")
    ax.set_ylabel("Nº Alertas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    path_img = "painel_grafico.png"
    plt.savefig(path_img)
    plt.close()
    return path_img
