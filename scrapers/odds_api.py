
import os
import requests
from typing import List, Dict

ODDS_API_KEY = os.getenv("ODDS_API_KEY")
BASE_URL = "https://api.the-odds-api.com/v4/sports/{sport}/odds/"

def fetch_odds_oddsapi(sport_key: str,
                       regions: str = "us",
                       markets: str = "h2h,spreads,totals") -> List[Dict]:
    """Obtém odds do The Odds API.

    Args:
        sport_key: Exemplo 'basketball_nba', 'americanfootball_nfl', 'baseball_mlb'.
        regions: Mercado/região (us, uk, eu).
        markets: Tipos de mercado.
    Returns:
        Lista de partidas com odds.
    """
    if not ODDS_API_KEY:
        raise EnvironmentError("Defina ODDS_API_KEY no ambiente.")

    url = BASE_URL.format(sport=sport_key)
    params = {
        "apiKey": ODDS_API_KEY,
        "regions": regions,
        "markets": markets,
        "oddsFormat": "decimal"
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()
