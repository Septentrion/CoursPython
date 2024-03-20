# Les « Dataclass »

## Introduction

Python 3.7 introduit la notion de « dataclass » (ou « classe de données »), dont le rôle est, comme sonnom l'indique de contenir des données, bien qu'il n'y ait pas vraiment de restrictions sur la structure de ces classes.

C'est l'une des (nombreuses) manières de structurer des données en Python. Citons : typing. NamedTuple, namedlist, attrdict, plumber, fields, etc.

## Création d'une classe

Une _dataclass_ se caractérise :
1. par le décorateur `@dataclass`
2. par l'emploi de types pour les données

```python
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float
```
La notation `:` pour les propriétés a été introduite avec Python 3.6 et s'appelle « _annotation de variable_ ». Comme partout en Python, elle est consultative et ne sert que pour les analyseurs statiques de code comm `mypy`.

Pour le reste, une _dataclass_ est une classe comme les autres, si ce n'est que certaines méthodes magiques, comme `__init__`, `__repr__`, `__eq__` sont implémentées d'office par ces classes (elles peuvent néanmoins être surchargées).

### Méthodes

Rien d'empêche d'ajouter des méthodes à ces classes, exactement comme nous le ferions ordinairement. Ajoutons une méthode pour calculer la distance entre deux points du globe :
```python
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

    def distance_to(self, other):
            r = 6371  # Earth radius in kilometers
            lam_1, lam_2 = radians(self.lon), radians(other.lon)
            phi_1, phi_2 = radians(self.lat), radians(other.lat)
            h = (sin((phi_2 - phi_1) / 2)**2
                 + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
            return 2 * r * asin(sqrt(h))
```

## Spécificités des _dataclasses_

### Spécifieur field

Les classes admettent des valeurs par défaut. Celles-ci sont associées à des options. Pour en spécifier l'ensemble, on utilisera un « constructeur »: `field`. Il se révèle indispensable si vous avez de valeurs par défaut _mutables_, mais offre aussi d'autres fonctionnalités.
- `default` : une valeur par défaut constante
- `default_factory` : une valeur par défaut mutable (calculée)
- `init` : initialisée par le constructeur de la classe
- `repr` : prise en compte par `__repr__`
- `compare`: est utilisée lors de la comparaison entre objets
- `hash` : utilisée pour calculer un « hash »
- `metadata` : information à propos de la propriété

```python
from dataclasses import dataclass, field

@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})
```

### Comparaison entre objets

Pour pouvoir comparer des objets, il faut les ordonner. Pour cela, les _dataclasses_ offrent une option du décorateur :
```python
@dataclass(order=True)
```
Dans une deuxième étape, il faut définir un ordre sur les valeurs. Cela nécessite d'ajouter dux éléments à la classe :
- une propriété `sort_index` qui contient la valeur de l'ordre
- une méthode `__post_init__` qui calcule cette valeur

Pour comparer les cartes d'un jeu de cartes traditionnel, apr exmple :
```python
from dataclasses import dataclass, field

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))
```

### Immutabilité

Une autre option du décorateur permet de rendre l'objet immutable :
```python
@dataclass(frozen=True)
```
Désormais, les valeurs ne peuvent plus être modifiées et se comportent donc comme des constantes.
```python
from dataclasses import dataclass, field

@dataclass(froze=True)
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})

oslo = Position('Oslo', 10.8, 59.9)
# Illégal
# oslo.lon = 10.85
```

## Ressources :
- [Documentation Real Python](https://realpython.com/python-data-classes/)
-
