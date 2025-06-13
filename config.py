
"""Configurações e helpers para variáveis de ambiente"""
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_env(var_name: str, default: str = None):
    value = os.getenv(var_name, default)
    if value is None:
        raise EnvironmentError(f"Variável {var_name} não definida e sem default.")
    return value
