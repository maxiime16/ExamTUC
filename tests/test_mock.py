import unittest
from unittest.mock import MagicMock, patch
from sqlalchemy.orm import Session
from app import actions, models, schemas
from app.utils.pokeapi import get_pokemon_name
from app.routers.items import *
from app.routers.pokemons import *
from app.routers.trainers import *
from app import *


class TestActions(unittest.TestCase):
    def setUp(self):
        self.database = MagicMock(spec=Session)
    
    def test_get_trainer(self):
        # Setup
        trainer_id = 1
        trainer = models.Trainer(id=trainer_id, name="Ash", birthdate="1990-01-01")
        self.database.query.return_value.filter.return_value.first.return_value = trainer

        # Test
        result = actions.get_trainer(self.database, trainer_id)

        # Assertions
        self.assertEqual(result, trainer)

    def test_get_trainer_by_name(self):
        # Setup
        name = "Ash"
        trainers = [models.Trainer(id=1, name=name, birthdate="1990-01-01")]
        self.database.query.return_value.filter.return_value.all.return_value = trainers

        # Test
        result = actions.get_trainer_by_name(self.database, name)

        # Assertions
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, name)

    def test_get_trainers(self):
        # Setup
        trainers = [models.Trainer(id=1, name="Ash", birthdate="1990-01-01")]
        self.database.query.return_value.offset.return_value.limit.return_value.all.return_value = trainers

        # Test
        result = actions.get_trainers(self.database)

        # Assertions
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Ash")

    def test_create_trainer(self):
        # Setup
        trainer_data = schemas.TrainerCreate(name="Ash", birthdate="1990-01-01")
        new_trainer = models.Trainer(id=1, name=trainer_data.name, birthdate=trainer_data.birthdate)
        self.database.add.return_value = None
        self.database.commit.return_value = None
        self.database.refresh.return_value = new_trainer
        # Test
        result = actions.create_trainer(self.database, trainer_data)
    
        # Assertions
        self.assertEqual(result.name, "Ash")
        self.assertEqual(result.birthdate.isoformat(), "1990-01-01")

    def test_add_trainer_pokemon(self):
        # Setup
        pokemon_data = schemas.PokemonCreate(api_id=25)
        trainer_id = 1
        new_pokemon = models.Pokemon(
            **pokemon_data.model_dump(),
            name=get_pokemon_name(pokemon_data.api_id),
            trainer_id=trainer_id
        )
        actions.get_pokemon_name = MagicMock(return_value="Pikachu")
        self.database.add.return_value = None
        self.database.commit.return_value = None
        self.database.refresh.return_value = None

        # Test
        result = actions.add_trainer_pokemon(self.database, pokemon_data, trainer_id)

        # Assertions
        self.assertEqual(result.api_id, 25)
        self.assertEqual(result.name, "Pikachu")
        self.assertEqual(result.trainer_id, trainer_id)

    def test_add_trainer_item(self):
        # Setup
        item_data = schemas.ItemCreate(name="Potion", description="Restores 20 HP")
        trainer_id = 1
        new_item = models.Item(
            **item_data.model_dump(),
            trainer_id=trainer_id
        )
        self.database.add.return_value = None
        self.database.commit.return_value = None
        self.database.refresh.return_value = None

        # Test
        result = actions.add_trainer_item(self.database, item_data, trainer_id)

        # Assertions
        self.assertEqual(result.name, "Potion")
        self.assertEqual(result.description, "Restores 20 HP")
        self.assertEqual(result.trainer_id, trainer_id)

    def test_get_items(self):
        # Setup
        items = [models.Item(id=1, name="Potion", description="Restores 20 HP", trainer_id=1)]
        self.database.query.return_value.offset.return_value.limit.return_value.all.return_value = items

        # Test
        result = actions.get_items(self.database)

        # Assertions
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Potion")
        self.assertEqual(result[0].description, "Restores 20 HP")

    def test_get_pokemon(self):
        # Setup
        pokemon_id = 25
        pokemon = models.Pokemon(id=pokemon_id, api_id=25, name="Pikachu", trainer_id=1)
        self.database.query.return_value.filter.return_value.first.return_value = pokemon

        # Test
        result = actions.get_pokemon(self.database, pokemon_id)

        # Assertions
        self.assertEqual(result, pokemon)

    def test_get_pokemons(self):
        # Setup
        pokemons = [models.Pokemon(id=1, api_id=25, name="Pikachu", trainer_id=1)]
        self.database.query.return_value.offset.return_value.limit.return_value.all.return_value = pokemons

        # Test
        result = actions.get_pokemons(self.database)

        # Assertions
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Pikachu")

if __name__ == '__main__':
    unittest.main()
