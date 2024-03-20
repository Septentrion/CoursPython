# Les constantes en Python

## Introduction

Python ne définit pas directement la notion de constante. D'une manière générale, les symboles sont des variables.

Néanmoins, il existe quelques techniques pour créer des valeurs immutables.

> Rappelons que, en référence à la programmation fonctionnelle, il ne devrait exister _que des variabmles immutables_, ou des mécanismes permettant de protéger les variables lorsque les valeurs changent (comme en Rust, par exemple).

D'une manière générale, les soi-disant constantes dans les programmes Python sont purement conventionnelles (de même que les propriétés « privées » des classes). On les note en majuscules pou _prévenir_ le lecteur qu'il ne doit pas modifier la valeur. MAis ce ci est purement indicatif.
```python
MAX_SPEED = 300
DEFAULT_COLOR = "\033[1;34m"
API_TOKEN = "593086396372"
ALLOWED_BUILTINS = ("sum", "max", "min", "abs")
```

## Comment créer des constantes ?

Il existe plusieurs manières de créer des constantes. Malheureusement, il faudra la plupart du temps recourir à des structures de données complexes.

### Les tuples nommés

Les tuples sont par nature des structures de données immutables. En utilsant leur variante nommée, il est possible de créer une liste de constantes :
```python
from collections import namedtuple

ConstantsNamespace = namedtuple("ConstantsNamespace", ["PI", "EULER_NUMBER"])
constants = ConstantsNamespace(3.141592653589793, 2.718281828459045)

print(constants.PI)
# 3.141592653589793
print(constants.EULER_NUMBER)
# 2.718281828459045
```

### Les dataclasses gelées

Les _dataclasses_ admettent une oprion `frozen` qui rend leur propriétés immutables. C'est donc également une possibilité :
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ConstantsNamespace:
    PI = 3.141592653589793
    EULER_NUMBER = 2.718281828459045

constants = ConstantsNamespace()

print(constants.PI)
# 3.141592653589793
print(constants.EULER_NUMBER)
# 2.718281828459045
```

### La méthode magique `__setattr__`

Les classes traditionnelles disposent de méthodes « magiques », qui ouvrent sur une forme de méta-programmation.

Ainsi, `__setattr__` permet de spécifier ce qui se passe si l'on essaie de modifier la valeur d'un attribut. Il serait donc possible d'écrire :
```python
class ConstantsNamespace:
    PI = 3.141592653589793
    EULER_NUMBER = 2.718281828459045
    def __setattr__(self, name, value):
        raise AttributeError(f"can't reassign constant '{name}'")
```
Toute tentative de modification déclenche maintenant une exception.

### Le décorateur @property

En utilisatn `@property`, nous transformons une méthode en propriété (du moins vue de l'extérieur). C'est une technique qui permet de pourvoir les classes de propriétés privées. En effet, l'usage de `@property` implique de définir un mutateur (aui pourrait être `PI.setter` dans l'exemple ci-dessous). En son absence, la valeur est immutable.

```python
>>> class ConstantsNamespace:
...     @property
...     def PI(self):
...         return 3.141592653589793
...     @property
...     def EULER_NUMBER(self):
...         return 2.718281828459045
...

>>> constants = ConstantsNamespace()
```

### La propriété magique `__slots__`

Les classes possèdent enfin une propriété `__slots__`, qui est une alternative à `__dict__`, un dictionnaire qui recense toutes les propriétés de l'objet.

`__slots__` empêche la création de `__dict__`.

Si l'on déclare un `__slots__` vide, alors nous n'aurons plus accès aux propriétés pour les modifier.
```python
class ConstantsNamespace:
    __slots__ = ()
    PI = 3.141592653589793
    EULER_NUMBER = 2.718281828459045

constants = ConstantsNamespace()
```

## Ressources

- [Documentation Real Python](https://realpython.com/python-constants/#defining-strict-constants-in-python)
