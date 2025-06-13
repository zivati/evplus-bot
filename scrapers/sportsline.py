
import requests
from bs4 import BeautifulSoup

def get_sportsline_predictions(league: str):
    '''
    Coleta previsões da Sportsline para uma liga específica.
    Ligas suportadas: nba, nfl, mlb, ncaaf, ncaab
    '''
    url_map = {
        'nba': 'https://www.sportsline.com/nba/picks/',
        'nfl': 'https://www.sportsline.com/nfl/picks/',
        'mlb': 'https://www.sportsline.com/mlb/picks/',
        'ncaaf': 'https://www.sportsline.com/college-football/picks/',
        'ncaab': 'https://www.sportsline.com/college-basketball/picks/',
    }

    url = url_map.get(league.lower())
    if not url:
        raise ValueError('Liga inválida. Use: nba, nfl, mlb, ncaaf, ncaab')

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    predictions = []
    games = soup.select('.prediction-pick-card')

    for game in games:
        try:
            teams = game.select_one('.prediction-pick-matchup').get_text(separator='vs').split('vs')
            pick = game.select_one('.prediction-pick-picktext')
            if teams and pick:
                predictions.append({
                    'team_1': teams[0].strip(),
                    'team_2': teams[1].strip(),
                    'prediction': pick.text.strip()
                })
        except Exception as e:
            print(f"Erro ao processar jogo: {e}")
            continue

    return predictions
