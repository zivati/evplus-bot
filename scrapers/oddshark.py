
import requests
from bs4 import BeautifulSoup

def get_predicted_scores(league: str):
    '''
    Coleta os placares previstos do Oddshark para uma liga específica (NBA, NFL, MLB, NCAAF, NCAAB)
    league: 'nba', 'nfl', 'mlb', 'ncaaf', 'ncaab'
    '''
    url_map = {
        'nba': 'https://www.oddsshark.com/nba/computer-picks',
        'nfl': 'https://www.oddsshark.com/nfl/computer-picks',
        'mlb': 'https://www.oddsshark.com/mlb/computer-picks',
        'ncaaf': 'https://www.oddsshark.com/ncaaf/computer-picks',
        'ncaab': 'https://www.oddsshark.com/ncaab/computer-picks',
    }

    url = url_map.get(league.lower())
    if not url:
        raise ValueError('Liga inválida. Use: nba, nfl, mlb, ncaaf, ncaab')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    picks = []
    games = soup.select('.op-matchup-wrapper')

    for game in games:
        try:
            teams = game.select('.op-matchup-team-name')
            scores = game.select('.op-pick-result .op-score')

            if len(teams) == 2 and len(scores) == 2:
                pick_data = {
                    'team_1': teams[0].text.strip(),
                    'team_2': teams[1].text.strip(),
                    'score_1': float(scores[0].text.strip()),
                    'score_2': float(scores[1].text.strip()),
                }
                picks.append(pick_data)
        except Exception as e:
            print(f"Erro ao processar jogo: {e}")
            continue

    return picks
