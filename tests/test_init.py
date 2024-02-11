import pytest
from ..app.utils.pokeapi import get_pokemon_name

def test_get_pokemon_name():
    api_id = 1
    pokemon_name = get_pokemon_name(api_id)
    assert pokemon_name == 'bulbasaur'