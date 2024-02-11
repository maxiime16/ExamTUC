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

************* Module TP_tuc_examen.app.models
app/models.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app/models.py:6:0: R0903: Too few public methods (0/2) (too-few-public-methods)
app/models.py:27:0: R0903: Too few public methods (0/2) (too-few-public-methods)
app/models.py:50:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module TP_tuc_examen.app.actions
app/actions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module TP_tuc_examen.app.sqlite
app/sqlite.py:9:0: C0304: Final newline missing (missing-final-newline)
app/sqlite.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app/sqlite.py:5:0: C0103: Constant name "sqlite_url" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module TP_tuc_examen.app.schemas
app/schemas.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app/schemas.py:8:0: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:12:0: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:15:0: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:19:4: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:19:4: R0903: Too few public methods (0/2) (too-few-public-methods)
app/schemas.py:25:0: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:29:0: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:32:0: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:37:4: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:37:4: R0903: Too few public methods (0/2) (too-few-public-methods)
app/schemas.py:42:0: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:46:0: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:49:0: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:54:4: C0115: Missing class docstring (missing-class-docstring)
app/schemas.py:54:4: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module TP_tuc_examen.app.routers.pokemons
app/routers/pokemons.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app/routers/pokemons.py:4:0: E0401: Unable to import 'app' (import-error)
app/routers/pokemons.py:5:0: E0401: Unable to import 'app.utils.utils' (import-error)
************* Module TP_tuc_examen.app.routers.trainers
app/routers/trainers.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app/routers/trainers.py:4:0: E0401: Unable to import 'app.utils.utils' (import-error)
app/routers/trainers.py:5:0: E0401: Unable to import 'app' (import-error)
************* Module TP_tuc_examen.app.routers.items
app/routers/items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app/routers/items.py:4:0: E0401: Unable to import 'app.utils.utils' (import-error)
app/routers/items.py:5:0: E0401: Unable to import 'app' (import-error)
************* Module TP_tuc_examen.app.utils.pokeapi
app/utils/pokeapi.py:38:0: C0301: Line too long (110/100) (line-too-long)
app/utils/pokeapi.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app/utils/pokeapi.py:3:0: C0103: Constant name "base_url" doesn't conform to UPPER_CASE naming style (invalid-name)
app/utils/pokeapi.py:35:4: C0103: Variable name "premierPokemon" doesn't conform to snake_case naming style (invalid-name)
app/utils/pokeapi.py:36:4: C0103: Variable name "secondPokemon" doesn't conform to snake_case naming style (invalid-name)
app/utils/pokeapi.py:41:25: W0613: Unused argument 'first_pokemon_stats' (unused-argument)
app/utils/pokeapi.py:41:46: W0613: Unused argument 'second_pokemon_stats' (unused-argument)
************* Module TP_tuc_examen.app.utils.utils
app/utils/utils.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app/utils/utils.py:2:0: E0401: Unable to import 'app' (import-error)
app/utils/utils.py:3:0: E0401: Unable to import 'app.sqlite' (import-error)

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


