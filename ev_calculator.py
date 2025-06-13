
def implied_probability_from_odds(odds: float) -> float:
    """
    Converte odds decimais em probabilidade implícita
    """
    return 1 / odds if odds > 0 else 0

def ev_percent(model_probability: float, market_odds: float) -> float:
    """
    Calcula o EV% baseado na probabilidade do modelo e odds de mercado
    model_probability: probabilidade prevista pelo modelo (entre 0 e 1)
    market_odds: odds decimais do mercado (ex: 2.10)
    """
    market_prob = implied_probability_from_odds(market_odds)
    if market_prob == 0:
        return 0
    return round(((model_probability / market_prob) - 1) * 100, 2)

def compare_lines(predicted_score_1, predicted_score_2, market_line: float, tipo: str = 'spread') -> float:
    """
    Estima probabilidade do modelo vencer a linha
    tipo = 'spread' ou 'total'
    """
    if tipo == 'spread':
        expected_diff = predicted_score_1 - predicted_score_2
        if expected_diff > market_line:
            return 0.55  # arbitrário inicial até termos dist. prob
        elif expected_diff == market_line:
            return 0.50
        else:
            return 0.45
    elif tipo == 'total':
        expected_total = predicted_score_1 + predicted_score_2
        if expected_total > market_line:
            return 0.55
        elif expected_total == market_line:
            return 0.50
        else:
            return 0.45
    else:
        return 0.0
