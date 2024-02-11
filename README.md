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

> Pylint au début du projet:
 - Module TP_tuc_examen.app.models: C0114, R0903
 - Module TP_tuc_examen.app.actions: C0114
 - Module TP_tuc_examen.app.sqlite: C0304, C0114, C0103
 - Module TP_tuc_examen.app.schemas: C0114, C0115, R0903
 - Module TP_tuc_examen.app.routers.pokemons: C0114, E0401
 - Module TP_tuc_examen.app.routers.trainers: C0114, E0401
 - Module TP_tuc_examen.app.routers.items: C0114, E0401
 - Module TP_tuc_examen.app.utils.pokeapi: C0301, C0114, C0103, W0613
 - Module TP_tuc_examen.app.utils.utils: C0114, E0401

> Ajouts fait:
 - C0114 | C0115 | C0116: ajouts de docstring aux modules, class et fonctions
 - R0903: ajouts de methodes (__repr__ ; to_dict ...)
 - C0103: Mettre ma variable en majuscules
 - C0304: Derniere ligne manquante
 - E0401: Changement du chemin d'importation
 - C0301: ligne trop longue
 - C0103: Changement en variable conforme

Avancement: 🟢 note > 9.5

### Unittest
Groupe de 3
5 tests unitaires
3 tests unitaires mocks

Avancement: 🔴

### Coverage
Groupe de 3
> 80% de code couvert par vos tests

Avancement: 🔴

