"""
Module contenant des fonctions pour interagir avec l'API PokeAPI.
"""

import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
    Obtenir le nom d'un Pokémon à partir de l'API PokeAPI.
    """
    return get_pokemon_data(api_id)['name']


def get_pokemon_stats(api_id):
    """
    Obtenir les statistiques d'un Pokémon à partir de l'API PokeAPI.
    """
    response = requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10)
    response.raise_for_status()
    stats = response.json()['stats']

    base_stats = [stat['base_stat'] for stat in stats]

    return base_stats


def get_pokemon_data(api_id):
    """
    Obtenir les données d'un Pokémon à partir de l'API PokeAPI.
    """
    return requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
    Effectuer un combat entre deux Pokémon.
    """
    first_pokemon = get_pokemon_data(first_api_id)
    second_pokemon = get_pokemon_data(second_api_id)

    first_pokemon_stats = get_pokemon_stats(first_api_id)
    second_pokemon_stats = get_pokemon_stats(second_api_id)

    battle_result = battle_compare_stats(first_pokemon_stats, second_pokemon_stats)

    if battle_result > 0:
        return first_pokemon
    return second_pokemon if battle_result < 0 else {'winner': 'draw'}


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
    Compare les statistiques données entre deux Pokémon.
    
    """
    resultat = 0
    for i in range(6):
        if first_pokemon_stats[i] > second_pokemon_stats[i]:
            resultat += 1
        if first_pokemon_stats[i] < second_pokemon_stats[i]:
            resultat -= 1
        else:
            resultat += 0
    return resultat
