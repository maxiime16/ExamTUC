import pytest
from datetime import date
from fastapi.testclient import TestClient

from app.utils.pokeapi import *
from app.utils.utils import *

from main import app

client = TestClient(app)

#
# Tests pokeapi.py
#

api_id_1 = 10
api_id_2 = 25
api_id_3 = 150
api_stat_1 = [45, 30, 35, 20, 20, 45]
api_stat_2 = [35, 55, 40, 50, 50, 90]
api_stat_3 = [106, 110, 90, 154, 90, 130]

def test_get_pokemon_name():
    assert get_pokemon_name(api_id_2) == "pikachu"
    assert get_pokemon_name(api_id_3) == "mewtwo"

def test_get_pokemon_stats():
    assert get_pokemon_stats(api_id_2) == [35, 55, 40, 50, 50, 90]
    assert get_pokemon_stats(api_id_3) == [106, 110, 90, 154, 90, 130]

def test_battle_compare_stats():
    assert battle_compare_stats(api_stat_3, api_stat_2) == 6
    assert battle_compare_stats(api_stat_1, api_stat_1) == 0
    assert battle_compare_stats(api_stat_1, api_stat_2) == -4

def test_battle_pokemon():
    assert battle_pokemon(api_id_1, api_id_2)['id'] == 25
    assert battle_pokemon(api_id_3, api_id_2)['id'] == 150
    assert battle_pokemon(api_id_1, api_id_1) == {'winner': 'draw'}


#
# Test utils.py
#

def test_age_from_birthdate():
    birthdate = date(1990, 1, 15)
    today = date.today()

    assert age_from_birthdate(birthdate) == 34
    assert age_from_birthdate(today) == 0

def test_get_db():
    db = next(get_db())
    assert db is not None


#
# Test trainers.py
#

def test_create_trainer():
    trainer_data = {
        "name": "Ash",
        "birthdate": "1990-01-01"
    }
    response = client.post("/trainers/", json=trainer_data)
    assert response.status_code == 200
    created_trainer = response.json()
    assert created_trainer["name"] == trainer_data["name"]

def test_get_trainers():
    response = client.get("/trainers")
    assert response.status_code == 200
    trainers = response.json()
    assert len(trainers) > 0

def test_get_trainer():
    trainer_id = 1
    response = client.get(f"/trainers/{trainer_id}")
    assert response.status_code == 200
    retrieved_trainer = response.json()
    assert retrieved_trainer["id"] == trainer_id

def test_create_item_for_trainer():
    trainer_id = 1
    item_data = {
        "name": "Potion",
        "description": "Restores 20 HP"
    }
    response = client.post(f"/trainers/{trainer_id}/item/", json=item_data)
    assert response.status_code == 200
    created_item = response.json()
    assert created_item["name"] == item_data["name"]

def test_create_pokemon_for_trainer():
    # Test d'ajout d'un Pokémon à un entraîneur
    trainer_id = 1
    pokemon_data = {
        "api_id": 25
    }
    response = client.post(f"/trainers/{trainer_id}/pokemon/", json=pokemon_data)
    assert response.status_code == 200
    created_pokemon = response.json()
    assert created_pokemon["api_id"] == pokemon_data["api_id"]
