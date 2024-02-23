# TUC EXAM

## Membres du groupe:
- Enzo De Sousa
- Mathieu Cellier
- Maxime Devillepoix

## Installation:
> pip install
```
pip install fastapi locust pytest uvicorn coverage httpx pytest-mock pytest-profiling pylint sqlalchemy pydantic
```
## Run:
> FastAPI
 - ```uvicorn main:app --reload```
 - ```http://127.0.0.1:8000/docs```

> Locust
 - ```locust -f <test_file.py>``` (ici locust -f tests/load_test.py)
 - ```http://0.0.0.0:8089```

> Pylint
 - ```pylint app```

> Coverage 
    ```coverage run -m pytest ```
    ```coverage report -m```

## Changements fait:
### Code:
> Création d'un endpoint qui permet de faire combattre 2 pokémons en fournissant leur ID

> Comparez chaque stats des 2 pokemons 1 par 1

### Locust:
> Scénario pertinant (voir .locust.conf.)

> Exemple de test

### Pylint:
> Note > 9.5

> Changements du code:
 - Ajouts de docstring aux modules, class et fonctions
 - Ajouts de methodes
 - Changement de typographie
 - etc...

### Unittest:
> Création de plusieurs tests unitaires (test_init.py)

> Création de plusieurs tests unitaires mocks (test_mock.py)

### Coverage:
> Coverage > 90%