
import os
import requests
from typing import List, Dict

API_SPORTS_KEY = os.getenv("API_SPORTS_KEY")
BASE_URL_MAP = {
    "nba": "https://v3.basketball.api-sports.io/odds",
    "nfl": "https://v3.american-football.api-sports.io/odds",
    "mlb": "https://v3.baseball.api-sports.io/odds"
}

def fetch_odds_apisports(league: str, date: str = None) -> List[Dict]:
    """Obtém odds do API-SPORTS.

    Args:
        league: 'nba', 'nfl', 'mlb'
        date: YYYY-MM-DD (opcional; default hoje)
    Returns:
        Lista de partidas com odds.
    """
    if not API_SPORTS_KEY:
        raise EnvironmentError("Defina API_SPORTS_KEY no ambiente.")

    url = BASE_URL_MAP.get(league.lower())
    if not url:
        raise ValueError("Liga inválida para API-SPORTS.")

    headers = {
        "x-apisports-key": API_SPORTS_KEY
    }
    params = {}
    if date:
        params["date"] = date

    resp = requests.get(url, headers=headers, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json().get("response", [])
