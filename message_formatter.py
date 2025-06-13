
def gerar_analise_jogo(jogo: dict) -> str:
    """
    Recebe dados consolidados de um jogo e retorna uma string formatada para envio
    """
    time_1 = jogo['team_1']
    time_2 = jogo['team_2']
    ev_percentual = jogo['ev_percent']
    score_conf = jogo['score_confidence']
    mercado_odds = jogo['market_odds']
    tipo_aposta = jogo['tipo']  # ex: spread, total, ml
    linha_mercado = jogo['linha_mercado']
    pick_modelo = jogo['pick_modelo']

    if ev_percentual >= 5 and score_conf >= 7:
        status = "🟢 EV+"
    elif ev_percentual > 0:
        status = "⚠️ EV0"
    else:
        status = "🔴 EV-"

    return f"""{status} {time_1} vs {time_2}
Aposta: {tipo_aposta.upper()} ({pick_modelo})
Linha de mercado: {linha_mercado} | Odds: {mercado_odds}
EV%: {ev_percentual:.2f}% | Score de Confiança: {score_conf}/10
"""

def gerar_analise_dia(jogos: list) -> str:
    """
    Gera a análise completa do dia a partir da lista de jogos
    """
    relatorio = ["📊 Análise completa do dia:\n"]
    for jogo in jogos:
        relatorio.append(gerar_analise_jogo(jogo))
    return "\n".join(relatorio)
