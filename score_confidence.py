
def calcular_score_confiança(
    forma_recente: float,         # 0 a 10 baseado nos últimos 10 jogos
    eficiencia_ofensiva: float,   # 0 a 10
    eficiencia_defensiva: float,  # 0 a 10
    lesoes_impactantes: int,      # número de jogadores importantes fora
    sharp_money: bool,            # se há convergência com dinheiro inteligente
    convergencia_modelos: bool    # se Oddshark e Sportsline batem
) -> float:
    """
    Retorna um score de confiança de 0 a 10
    """
    peso_forma = 0.20
    peso_of = 0.20
    peso_df = 0.20
    peso_lesoes = 0.20
    peso_sharp = 0.10
    peso_modelos = 0.10

    lesoes_score = max(0, 10 - lesoes_impactantes * 2)

    score = (
        forma_recente * peso_forma +
        eficiencia_ofensiva * peso_of +
        eficiencia_defensiva * peso_df +
        lesoes_score * peso_lesoes +
        (10 if sharp_money else 5) * peso_sharp +
        (10 if convergencia_modelos else 5) * peso_modelos
    )

    return round(score, 2)
