# Gestion des exceptions en Python

Ce dossier regroupe des exercices sur la gestion des exceptions en Python :
lever une exception, intercepter des erreurs prévisibles et garantir
l'exécution d'un bloc avec `finally`.

## Objectifs

- comprendre la différence entre `try`, `except` et `finally` ;
- lever une exception avec `raise` ;
- intercepter uniquement les exceptions attendues ;
- retourner une valeur utile après une erreur au lieu d'interrompre le programme ;
- parcourir une liste sans dépasser ses limites.

## Fichiers

| Fichier | Fonction | Rôle |
| --- | --- | --- |
| `raise_exception.py` | `raise_exception()` | lève systématiquement une `TypeError` ; |
| `raise_exception_msg.py` | `raise_exception_msg(message="")` | lève une `NameError` avec le message fourni ; |
| `safe_print_integer.py` | `safe_print_integer(value)` | affiche un entier et retourne `True`, sinon retourne `False` ; |
| `safe_print_list.py` | `safe_print_list(my_list=[], x=0)` | affiche au plus `x` éléments et retourne le nombre d'éléments affichés ; |
| `safe_print_list_integers.py` | `safe_print_list_integers(my_list=[], x=0)` | affiche uniquement les valeurs entières valides et retourne leur nombre ; |
| `safe_print_division.py` | `safe_print_division(a, b)` | divise `a` par `b`, affiche le résultat interne et retourne le résultat ou `None` si `b` vaut zéro. |

## Utilisation

Depuis ce dossier, les fonctions peuvent être importées directement :

```bash
python3 -c "from safe_print_integer import safe_print_integer; print(safe_print_integer(42))"
```

Résultat :

```text
42
True
```

### Afficher un entier en toute sécurité

```python
from safe_print_integer import safe_print_integer

safe_print_integer(42)       # affiche 42 et retourne True
safe_print_integer("42")     # n'affiche rien et retourne False
```

### Parcourir une liste

```python
from safe_print_list import safe_print_list
from safe_print_list_integers import safe_print_list_integers

safe_print_list(["a", "b", "c"], 2)          # affiche ab, retourne 2
safe_print_list_integers([1, "x", 3], 3)       # affiche 13, retourne 2
```

Les fonctions ajoutent un retour à la ligne après le parcours. Si `x` est
supérieur à la longueur de la liste, l'itération s'arrête proprement à la fin
de celle-ci.

### Gérer une division par zéro

```python
from safe_print_division import safe_print_division

safe_print_division(10, 2)  # affiche "Inside result: 5.0", retourne 5.0
safe_print_division(10, 0)  # affiche "Inside result: None", retourne None
```

Le bloc `finally` affiche `Inside result` dans les deux cas.

### Lever des exceptions

```python
from raise_exception import raise_exception
from raise_exception_msg import raise_exception_msg

raise_exception()                 # lève TypeError
raise_exception_msg("message")    # lève NameError("message")
```

Pour observer une exception sans arrêter le script appelant, utilisez `try` / `except` :

```python
try:
	raise_exception_msg("entrée invalide")
except NameError as error:
	print(error)
```

## Prérequis

- Python 3 ;
- aucun paquet externe.

Vérifier la version installée :

```bash
python3 --version
```

## Vérification rapide

Chaque fichier peut être vérifié avec la compilation Python :

```bash
python3 -m py_compile *.py
```

La commande ne produit aucune sortie si la syntaxe est correcte.
