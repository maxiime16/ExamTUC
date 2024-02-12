"""
Ce module contient les tests pour l'application.
"""
import unittest
from datetime import date
from fastapi.testclient import TestClient
from ..app.utils.pokeapi import (
    get_pokemon_stats, get_pokemon_name,battle_compare_stats, battle_pokemon)
from ..app.utils.utils import age_from_birthdate, get_db
from ..main import app

client = TestClient(app)


class TestPokeAPI(unittest.TestCase):
    """Tests pour les fonctions utilitaires de PokeAPI."""

    api_id_1 = 10
    api_id_2 = 25
    api_id_3 = 150
    api_stat_1 = [45, 30, 35, 20, 20, 45]
    api_stat_2 = [35, 55, 40, 50, 50, 90]
    api_stat_3 = [106, 110, 90, 154, 90, 130]

    def test_get_pokemon_name(self):
        """Teste la fonction get_pokemon_name."""
        self.assertEqual(get_pokemon_name(self.api_id_2), "pikachu")
        self.assertEqual(get_pokemon_name(self.api_id_3), "mewtwo")

    def test_get_pokemon_stats(self):
        """Teste la fonction get_pokemon_stats."""
        self.assertEqual(get_pokemon_stats(self.api_id_2), [35, 55, 40, 50, 50, 90])
        self.assertEqual(get_pokemon_stats(self.api_id_3), [106, 110, 90, 154, 90, 130])

    def test_battle_compare_stats(self):
        """Teste la fonction battle_compare_stats."""
        self.assertEqual(battle_compare_stats(self.api_stat_3, self.api_stat_2), 6)
        self.assertEqual(battle_compare_stats(self.api_stat_1, self.api_stat_1), 0)
        self.assertEqual(battle_compare_stats(self.api_stat_1, self.api_stat_2), -4)

    def test_battle_pokemon(self):
        """Teste la fonction battle_pokemon."""
        self.assertEqual(battle_pokemon(self.api_id_1, self.api_id_2)['id'], 25)
        self.assertEqual(battle_pokemon(self.api_id_3, self.api_id_2)['id'], 150)
        self.assertEqual(battle_pokemon(self.api_id_1, self.api_id_1), {'winner': 'draw'})


class TestUtils(unittest.TestCase):
    """Tests pour les fonctions utilitaires dans utils.py."""

    def test_age_from_birthdate(self):
        """Teste la fonction age_from_birthdate."""
        birthdate = date(1990, 1, 15)
        today = date.today()

        self.assertEqual(age_from_birthdate(birthdate), 34)
        self.assertEqual(age_from_birthdate(today), 0)

    def test_get_db(self):
        """Teste la fonction test_get_db."""
        db = next(get_db())
        self.assertIsNotNone(db)


class TestTrainers(unittest.TestCase):
    """Tests pour les routes liées aux entraîneurs."""

    client = TestClient(app)

    def test_create_trainer(self):
        """Teste la route create_trainer."""
        trainer_data = {
            "name": "Ash",
            "birthdate": "1990-01-01"
        }
        response = self.client.post("/trainers/", json=trainer_data)
        self.assertEqual(response.status_code, 200)
        created_trainer = response.json()
        self.assertEqual(created_trainer["name"], trainer_data["name"])

    def test_get_trainers(self):
        """Teste la route get_trainers."""
        response = self.client.get("/trainers")
        self.assertEqual(response.status_code, 200)
        trainers = response.json()
        self.assertGreater(len(trainers), 0)

    def test_get_trainer(self):
        """Teste la route get_trainer."""
        trainer_id = 1
        response = self.client.get(f"/trainers/{trainer_id}")
        self.assertEqual(response.status_code, 200)
        retrieved_trainer = response.json()
        self.assertEqual(retrieved_trainer["id"], trainer_id)

    def test_create_item_for_trainer(self):
        """Teste la route create_item_for_trainer."""
        trainer_id = 1
        item_data = {
            "name": "Potion",
            "description": "Restaure 20 HP"
        }
        response = self.client.post(f"/trainers/{trainer_id}/item/", json=item_data)
        self.assertEqual(response.status_code, 200)
        created_item = response.json()
        self.assertEqual(created_item["name"], item_data["name"])

    def test_create_pokemon_for_trainer(self):
        """Teste la route create_pokemon_for_trainer."""
        trainer_id = 1
        pokemon_data = {
            "api_id": 25
        }
        response = self.client.post(f"/trainers/{trainer_id}/pokemon/", json=pokemon_data)
        self.assertEqual(response.status_code, 200)
        created_pokemon = response.json()
        self.assertEqual(created_pokemon["api_id"], pokemon_data["api_id"])


if __name__ == '__main__':
    unittest.main()
