"""Module contenant les définitions de schéma SQLAlchemy."""
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from .sqlite import Base


class Trainer(Base):
    """
        Classe représentant un dresseur de Pokémon.
    """
    __tablename__ = "trainers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birthdate = Column(Date)

    inventory = relationship("Item", back_populates="trainer")
    pokemons = relationship("Pokemon", back_populates="trainer")

    def __repr__(self):
        return f"<Dresseur id={self.id}, nom={self.name}>"

    def to_dict(self):
        """
        Convertit l'objet Dresseur en un dictionnaire.

        Retours:
            dict: Une représentation sous forme de dictionnaire de l'objet Dresseur.
        """
        return {
            "id": self.id,
            "nom": self.name,
            "date_naissance": self.birthdate.isoformat(),
            "inventaire": [item.to_dict() for item in self.inventory],
            "pokemons": [pokemon.to_dict() for pokemon in self.pokemons]
        }

class Pokemon(Base):
    """
        Classe représentant un Pokémon.
        Paramètres:
            api_id (int): ID provenant de l'API de Pokémon.
            name (str): Nom du Pokémon.
    """
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(Integer, index=True)
    name = Column(String, index=True)
    custom_name = Column(String, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))

    trainer = relationship("Trainer", back_populates="pokemons")

    def __repr__(self):
        return f"<Pokémon id={self.id}, nom={self.name}>"

    def to_dict(self):
        """
        Convertit l'objet Pokémon en un dictionnaire.

        Retours:
            dict: Une représentation sous forme de dictionnaire de l'objet Pokémon.
        """
        return {
            "id": self.id,
            "api_id": self.api_id,
            "nom": self.name,
            "nom_personnalisé": self.custom_name,
            "id_dresseur": self.trainer_id
        }

class Item(Base):
    """
        Classe représentant un objet dans l'inventaire d'un dresseur.
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))

    trainer = relationship("Trainer", back_populates="inventory")

    def __repr__(self):
        return f"<Objet id={self.id}, nom={self.name}>"

    def to_dict(self):
        """
        Convertit l'objet Objet en un dictionnaire.

        Retours:
            dict: Une représentation sous forme de dictionnaire de l'objet Objet.
        """
        return {
            "id": self.id,
            "nom": self.name,
            "description": self.description,
            "id_dresseur": self.trainer_id
        }
