"""
Module contenant les routes pour les Pokémon.
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from .. import actions, schemas
from ..utils.utils import get_db
from ..utils.pokeapi import battle_pokemon, get_random, get_pokemon_stats


router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Retourne tous les pokémons
        La limite par défaut est de 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons


@router.get("/battle/{first_pokemon_id}/{second_pokemon_id}")
def battle_pokemons(first_pokemon_id: int, second_pokemon_id: int,  database: Session = Depends(get_db)):
    """
        Battle entre 2 pokémons
    """  
    first_pokemon = actions.get_pokemon(database, first_pokemon_id)
    second_pokemon = actions.get_pokemon(database, second_pokemon_id)
    result_battle = battle_pokemon(first_pokemon.api_id, second_pokemon.api_id)
    if result_battle == first_pokemon.api_id:
        return "Victoire de: ",first_pokemon.name,first_pokemon
    if result_battle == second_pokemon.api_id:
        return "Victoire de: ",second_pokemon.name,second_pokemon
    else:
        return "match null"

@router.get("/random")
def get_3_randoms_pokemon():
    """
    Récupère une liste de 3 Pokémon aléatoires avec leurs statistiques.
    """
    random_pokemons = [get_random() for _ in range(3)]  # Obtient 3 Pokémon aléatoires
    pokemon_details = []
    
    for pokemon in random_pokemons:
        pokemon_id = pokemon['id']
        pokemon_name = pokemon['name']
        pokemon_stats = get_pokemon_stats(pokemon_id)
        pokemon_details.append({"name": pokemon_name, "stats": pokemon_stats})
    
    return pokemon_details
