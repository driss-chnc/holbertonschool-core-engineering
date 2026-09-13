# Python OOP

Ce projet regroupe une série d'exercices et d'exemples sur la programmation orientée objet en Python. Il est organisé en plusieurs dossiers pour progresser pas à pas dans les notions de classes, héritage, encapsulation, validation, abstractions et polymorphisme.

## Objectifs pédagogiques

- Comprendre le fonctionnement des classes et des objets en Python.
- Appliquer les principes de l'encapsulation.
- Maîtriser l'héritage simple et multiple.
- Utiliser les classes abstraites et les méthodes abstraites.
- Valider les données avec des contrôles de type et de valeur.
- Manipuler les propriétés, les méthodes spéciales et les représentations d'objets.

---

## Structure du projet

### 1. Dossier `abc/`

Ce dossier montre l'utilisation des classes abstraites et des mixins.

Contenu :
- `animals.py` : définition d'une classe abstraite `Animal` avec `Dog` et `Cat`.
- `dragon.py` : exemples de mixins `SwimMixin` et `FlyMixin` appliqués à une classe `Dragon`.
- `flyingfish.py` : démonstration de l'héritage multiple avec `Fish` et `Bird`.
- `shapes.py` : abstraction de formes géométriques avec `Shape`, `Circle` et `Rectangle`.
- `verboselist.py` : sous-classe de `list` qui affiche des messages lors des opérations de modification.

Concepts abordés :
- `ABC` et `abstractmethod`
- héritage multiple
- mixins
- polymorphisme
- classes abstraites

### 2. Dossier `classes_and_object_model/`

Ce dossier correspond à une progression dans la modélisation des classes et des objets.

Fichiers principaux :
- `0-square.py` : définition basique d'une classe `Square`.
- `1-square.py` : ajout d'un attribut `size` à l'initialisation.
- `2-square.py` : validation de la taille pour éviter les valeurs invalides.
- `3-square.py` : ajout de la méthode `area()`.
- `4-square.py` : mise en place des propriétés via `@property`.
- `5-square.py` : impression visuelle du carré avec `#`.
- `6-square.py` : gestion de la position du carré et méthode `__str__()`.
- `1-rectangle.py` et `2-rectangle.py` : versions de la classe `Rectangle` avec validation et calcul d'aire.

Concepts abordés :
- encapsulation
- validation d'attributs
- propriétés Python
- méthode `area()`
- méthode `__str__()`
- rendu visuel et affichage de formes

### 3. Dossier `inheritance/`

Ce dossier met l'accent sur l'héritage et la validation des données dans des classes géométriques.

Fichiers principaux :
- `base_geometry.py` : classe de base `BaseGeometry` avec `area()` et `integer_validator()`.
- `1-rectangle.py` : définition d'une classe `Rectangle` qui hérite de `BaseGeometry`.
- `1-square.py` : classe `Square` héritant d'un rectangle.
- `2-rectangle.py` : rectangle amélioré avec calcul d'aire et représentation textuelle.
- `2-square.py` : version de `Square` avec personnalisation de `__str__()`.

Concepts abordés :
- héritage
- validation des dimensions
- surcharge de méthodes
- construction de classes hiérarchiques
- représentation textuelle d'objets

---

## Répartition des notions par thème

### Classes et objets
Les classes sont utilisées dans tous les dossiers, avec des exemples simples et des cas plus avancés comme les carrés, rectangles, animaux ou formes géométriques.

### Encapsulation
Les attributs privés (`__size`, `__width`, `__height`) sont utilisés pour protéger les données et garantir leur intégrité via des validations.

### Héritage
Le dossier `inheritance/` est centré sur les relations entre classes, notamment la création de classes dérivées.

### Abstraction
Le dossier `abc/` introduit les concepts de classe abstraite et de méthode abstraite pour modéliser des comportements obligatoires.

### Polymorphisme
Les sous-classes redéfinissent des méthodes comme `area()`, `sound()`, `fly()`, `swim()` ou `__str__()` pour adapter le comportement à chaque type d'objet.

---

## Exemple de progression du projet

Le dépôt suit une logique d'apprentissage progressive :

1. Créer des classes simples.
2. Ajouter des attributs et validations.
3. Implémenter des méthodes métier comme `area()`.
4. Introduire les propriétés et l'encapsulation.
5. Utiliser l'héritage pour factoriser le code.
6. Explorer les classes abstraites et l'héritage multiple.

---

## Technologies utilisées

- Python 3
- Programmation orientée objet
- Classes, objets, attributs, méthodes
- Héritage, méthodes abstraites, mixins

---

## Conclusion

Ce dépôt est une base d'exercices de Python orientée objet, idéale pour apprendre progressivement la conception de classes, la gestion des données, l'héritage, les abstractions et le bon design d'application.

Il est particulièrement utile pour maîtriser les bases de la POO avant d'aborder des projets plus larges en Python.
