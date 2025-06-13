
import requests
from bs4 import BeautifulSoup

def get_pinnacle_odds_mock(league: str):
    '''
    Simulação da coleta de odds da Pinnacle por limitações de acesso real (exige API paga).
    Retorna odds simuladas com base na liga.
    '''
    # Em produção, substituir por API oficial ou scraping via intermediário
    return [
        {
            'team_1': 'Lakers',
            'team_2': 'Celtics',
            'spread_line': -3.5,
            'spread_odds': 1.91,
            'total_line': 221.5,
            'total_odds': 1.91,
            'ml_team_1': 1.80,
            'ml_team_2': 2.00
        },
        {
            'team_1': 'Yankees',
            'team_2': 'Red Sox',
            'spread_line': -1.5,
            'spread_odds': 1.95,
            'total_line': 8.5,
            'total_odds': 1.90,
            'ml_team_1': 1.70,
            'ml_team_2': 2.10
        }
    ]

def get_betfair_odds_mock(league: str):
    '''
    Simulação da coleta de odds da Betfair por limitações de scraping direto.
    '''
    return [
        {
            'team_1': 'Lakers',
            'team_2': 'Celtics',
            'ml_team_1': 1.85,
            'ml_team_2': 2.05
        },
        {
            'team_1': 'Yankees',
            'team_2': 'Red Sox',
            'ml_team_1': 1.72,
            'ml_team_2': 2.08
        }
    ]
