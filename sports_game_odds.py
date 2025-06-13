
import os
import requests
from typing import List, Dict

SGO_API_KEY = os.getenv("SGO_API_KEY")
BASE_URL = "https://sportsgameodds.com/api/odds"

def fetch_odds_sgo(league: str) -> List[Dict]:
    """Obtém odds via Sports Game Odds API (se disponível em free tier).

    Args:
        league: 'nba', 'nfl', 'mlb'
    Returns:
        Lista de partidas com odds.
    """
    if not SGO_API_KEY:
        raise EnvironmentError("Defina SGO_API_KEY no ambiente.")

    headers = {
        "x-api-key": SGO_API_KEY
    }
    params = {
        "league": league
    }
    resp = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json().get("data", [])
