# TUC EXAM

## Membres du groupe
- Enzo De Sousa
- Mathieu Cellier
- Maxime Devillepoix

## installation
- pip install
```
pip install fastapi locust pytest uvicorn coverage httpx pytest-mock pytest-profiling pylint sqlalchemy 
```

> FastAPI
- ```uvicorn main:app --reload```
- ```http://127.0.0.1:8000/docs```

> Locust
- ```locust -f <test_file.py>``` (ici locust -f tests/load_test.py)
- ```http://0.0.0.0:8089```


## choses a faire

### Code
> Création d'un endpoint qui permet de faire combattre 2 pokémons en fournissant leur ID.
Le combat : 
Comparez chaque stats des 2 pokemons 1 par 1 (health vs health, attack vs attack, etc ..)
Le Pokémon qui a le plus de stats supérieur gagne.
Avancement: 🔴

### Locust
Rédaction d'un scénario ( pertinent )
Un exemple de test de performance à réaliser fourni via un .locust.conf.
Avancement: 🟢

### Pylint
Groupe de 3
> Note minimal de 8/10
Avancement: 🔴

### Unittest
Groupe de 3
5 tests unitaires
3 tests unitaires mocks
Avancement: 🔴

### Coverage
Groupe de 3
> 80% de code couvert par vos tests
Avancement: 🔴


