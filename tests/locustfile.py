"""
Ce module contient les tests locust pour l'application.
"""
from locust import HttpUser, task, between

class Trainer(HttpUser):
    """
    Classe représentant un utilisateur simulé pour tester les performances des routes.
    """
    wait_time = between(2, 5)  # temps d'attente entre les tâches

    @task
    def get_trainer(self):
        """
        Tâche pour effectuer une requête GET pour récupérer un entraîneur.
        """
        self.client.get("/trainers/1")

    @task
    def create_item_for_trainer(self):
        """
        Tâche pour effectuer une requête POST pour créer un nouvel objet de type "item".
        """
        new_item = {
            "name": "Potion",
            "description": "Restores 20 HP",
        }
        self.client.post("/trainers/1/item/", json=new_item)
