from locust import HttpUser, task, between

class Trainer(HttpUser):
    wait_time = between(2,5) # temps d'attente entre les tâches

    @task
    def get_trainer(self):
        self.client.get("/trainers/1")

    @task
    def create_item_for_trainer(self):
        new_item = {
            "name": "Potion",
            "description": "Restores 20 HP",
        }
        self.client.post("/trainers/1/item/", json=new_item)