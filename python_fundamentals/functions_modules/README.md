# Python - Functions and Modules

Ce dossier contient des exercices d'introduction aux fonctions et aux modules
Python.

## Fichiers

| Fichier | Description |
| --- | --- |
| `islower.py` | Vérifie si un caractère est une lettre minuscule. |
| `pow.py` | Calcule la puissance `a` exposant `b`, y compris pour un exposant négatif. |
| `print_last_digit.py` | Affiche et retourne le dernier chiffre d'un nombre. |
| `uppercase.py` | Affiche une chaîne de caractères en majuscules. |
| `add.py` | Script de démonstration d'une addition avec la fonction `add`. |

## Utilisation

Les fonctions peuvent être importées depuis un autre script :

```python
from islower import islower
from pow import pow
from print_last_digit import print_last_digit
from uppercase import uppercase

print(islower("a"))          # True
print(pow(2, 3))             # 8
print_last_digit(98)         # Affiche 8 et retourne 8
uppercase("hello")           # Affiche HELLO
```

Pour exécuter un fichier directement :

```bash
python3 nom_du_fichier.py
```

`add.py` importe `add` depuis `add_0`. Ce module doit donc être présent dans le
même dossier avant d'exécuter ce script.

## Prérequis

- Python 3

## Vérification syntaxique

```bash
python3 -m py_compile *.py
```
