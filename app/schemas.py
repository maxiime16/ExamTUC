"""
Module contenant les schémas de données pour l'application.
"""

from datetime import date
from typing import List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#

class ItemBase(BaseModel):
    """
    Schéma de base pour un objet.
    """
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """
    Schéma pour la création d'un objet.
    """

class Item(ItemBase):
    """
    Schéma pour un objet.
    """
    id: int
    trainer_id: int

    class Config:
        """
        Configuration du schéma pour l'utilisation avec ORM.
        """
        orm_mode = True

#
#  POKEMON
#

class PokemonBase(BaseModel):
    """
    Schéma de base pour un Pokémon.
    """
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """
    Schéma pour la création d'un Pokémon.
    """

class Pokemon(PokemonBase):
    """
    Schéma pour un Pokémon.
    """
    id: int
    name: str
    trainer_id: int

    class Config:
        """
        Configuration du schéma pour l'utilisation avec ORM.
        """
        orm_mode = True

#
#  TRAINER
#

class TrainerBase(BaseModel):
    """
    Schéma de base pour un dresseur.
    """
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):
    """
    Schéma pour la création d'un dresseur.
    """

class Trainer(TrainerBase):
    """
    Schéma pour un dresseur.
    """
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        """
        Configuration du schéma pour l'utilisation avec ORM.
        """
        orm_mode = True
