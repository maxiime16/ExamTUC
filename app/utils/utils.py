"""
Module contenant des utilitaires pour l'application.
"""
from datetime import date
from ..sqlite import SessionLocal, engine
from .. import models

models.Base.metadata.create_all(bind=engine)

def get_db():
    """
    Obtenez la base de données.
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

def age_from_birthdate(birthdate):
    """
    Retourne l'âge à partir de la date de naissance.
    """
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day)
        < (birthdate.month, birthdate.day))
