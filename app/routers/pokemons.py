"""
Module contenant les routes pour les Pokémon.
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from .. import actions, schemas
from ..utils.utils import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Retourne tous les pokémons
        La limite par défaut est de 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons
