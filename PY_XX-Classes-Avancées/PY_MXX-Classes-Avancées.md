# Exercices sur les classes avancées

## Introduction

Python n'est pas un langage objet très évolué. Il est possible de définir des classes, mais il manque un certain nombre de caractéristiques pour en faire un « vrai » langage orienté-objet. Par exemple :

- les propriétés ne sont pas explicitment déclarées, mais créées « à la volée » dans le constructeur oules méthodes de la classe
- Il n'y a pas de distinction public/privé (pourtant une des bases de la POO)
- Il n'y a naturellement pas de types explicite
- Il n'y a pas non plus la possibilté de gérer des types génériques

Python devrait donc plutôt être considéré comme un langage impératif, muni de fonctinnalités orienté-objet.

### Rappels

#### Généralités

D'une manière générale, une classe — dans les langages à base de classes — est un paquetage de variables et de fonctions, répondant à trois principes :

1. l'**encapsulation**, c'est-à-dire le fait que la classe trace une frontière entre ce qui lui est propre et ce qui lui est étranger. La première vertu de l'encapsulation est la capacité à éviter les conflits de nommage. Deux fonctions peuvent porter le même nom, sans pour autant créer d'ambiguïté puizqu'elles sont déclarées dans des espaces différents. Une autre propriété essentielle de l'encapsulation est la distinction public/privé, qui permet de laisser à l'objet la possibilité de n'exposer qu'une partie de sa constitution et donc de ne laisser personne d'autre modifier des valeurs dont il a la responsabilité. C'est cette deuxième partie qui manque à Python.
2. l'**instanciation**, qui désigne le fait qu'une classe est une abstraction, dont le rôle est de servir de modèle aux objets concrets de l'application, qui zont les **instances**. Notons que dans une version étendue de la programmation orientée-objet, les classes sont elles-mêmes des instances d'autres classes, nommées **méta-classes**.
3. l'**envoi de message**, qui est le modèle d'exécution de ces langages. On dit qu'un objet _envoie un message_ à un autre objet et, qu'en retour, ce dernier envoie une réponse. Ce modèle est devenu moins visible dans les langages contemporains, mais reste très présente dans **SmallTalk**, par exemple.

Bien qu'il soit souvent considéré comme la pierre angulaire la de POO, l'**héritage** ne fait pas partie des caractéristiques fondamentales de ce paradigme. C'est d'ailleurs quelque chose qui est très critiqué et qu'il faut manipuler avec parcimonie. Comme nous le verrons plus loin, il y a un conflit historique entre les notions d'héritage (elle-même divisée en héritage simple et héritage multiple) et de composition.

## En Python

1. une classe se déclare par le mot-clef `class` :
```python
# Une classe qui ne fait rien
class Car :
  pass
```
2. Une instance est créée en appelant simplement la classe :
```python
c1 = Car()
```
3. Un message est envoyé à un objet avec la notation « pointée » :
```python
# Ceci est un exemple théorique puisque la méthode
# (ou fonction d'une classe) n'a pas encore été définie
x = c1.getColor()
```
4. Enfin si vous voulez hériter d'une autre classe, il suffit de déclarer cette dernière dans la signature de la nouvelle classe :
```python
class Car(Vehicle) :
  pass
```

Vous pouvez maintenant munir votre classe de toutes les méthodes nécessaires.
```python
class Car :

  # Les proprétés sont généralement déclarées
  # dans la fonction spéciale appelée « constructeur »
  def __init__(self, initialFuelVolume):
    self.color = "white"
    ## ATTENTION
    ## Le double __ ne signifie pas que la propriété est privée
    self.__speed = 0
    self.__tank = initialFuelVolume

  # Notez que les méthodes ont toujours aumoins un paramètre
  # qui est l'objet lui-même
  def fillTank(self) :
    # Notez la différence entre variable locale
    # et propriété d'instance
    volume = 100 - self.__tank
    self.__tank = 100

    return volume

my_car = Car(30)
# LA propriété est accessible dpuis l'extérieur
print(c1._Car__tank)
```

## Les propriétés des classes Python

## Héritage en Python

Le design informatique prônant la modularisation du code, il y a deux manières de voir le partage de ressources au sein d'un langage objet.

### Héritage : une pyramide taxonomique

La première manière consiste à mutualiser ce qui est commun sous la forme d'un arbre, souvent nommé **arbre de Porphyre** en référence aux premières tentatives grcques de classifier le vivant.

Les classes sont considérées comme des branches dans un arbre, la racine étant la classe la plus générique et les feuilles des classes finales.

C'est la vision traditionnelle de la POO à base de classes. Si elle est simple à comprendre, elle n'est pas sans défauts, surtout quand la profondeur de l'arbre commence à être importante.

#### Et l'héritage multiple ?

L'héritage multiple semble _a priori_ une solution séduisante. On transforme la pyramide de treillis, ce qui permet de gagner en souplesse de description.

Historiquement, assez peu de langages, à la suite de **SmallTalk**, permettent ce type de hiérarchie :

> C++, Python, Eiffel, Common Lisp, OCaml, Perl, entre autres

En réalité, cette forme d'héritage souffre de grave défauts d'indécidabilité, dont l'exemple le plus connu est le [diamant de Nixon](https://fr.wikipedia.org/wiki/Diamant_de_Nixon). C'est donc plutôt une fausse bonne idée.

> 1. Complexité : La gestion et la compréhension de multiples hiérarchies de classes peuvent rendre le code plus complexe et difficile à maintenir.
>
> 2. Risque de conflits : Lorsque deux classes parentes possèdent des méthodes ou des attributs portant le même nom, il peut y avoir des conflits d'héritage qui rendent le code moins fiable.
>
> 3. Dépendance excessive : L'héritage multiple peut entraîner une forte interdépendance entre différentes classes, ce qui peut rendre le code plus rigide et difficile à modifier.
>
> 4. Risque de confusion : Les multiples hiérarchies de classes peuvent entraîner une confusion quant à la logique de l'application et rendre le code moins intuitif pour les développeurs.
>
> 5. Difficulté de gestion : La gestion des relations entre les différentes classes et la résolution des problèmes de conception peuvent être plus compliquées avec l'héritage multiple, ce qui peut augmenter la charge de travail des développeurs.
>
> (Source GhatGPT)
>
> 6. L'héritage multiple génère parfois des erreurs de compilation. Lorsqu'une méthode polymorphique est appelée, il faut déduire la bonne implémentation à exécuter. Si la méthode est le résultat d'un héritage simple, elle n'a alors qu'une seule implémentation possible, et il ne sera donc pas difficile retrouver l'implémentation. Si la méthode est le résultat d'un héritage multiple, elle a alors plusieurs implémentations possibles. Il faut donc choisir l'une des implémentations concurrentes. C'est problématique car différentes implémentations peuvent avoir des effets de bord différents, résultant donc en un comportement indéfini (undefined behavior).

Pour résoudre ce problème, Python utilise un algorithme nommé MRO, qui résout les problèmes de conflits. Eiffel dispose aussi d'une telle stratégie. Mais, en général, on préférera d'autres solutions.

### Composition

A l'inverse de l'héritage, la composition n'est pas hiérarchique. Comme sont nom l'indique, il s'agir de composer une classe à partir d'éléments distincts, comme on compose un objet à partir de pièces détachées.

Il y a deux manières de faire de la composition.

#### Par les propriétés

La première manière de faire de la composition est relativements simple puisqu'elle utilise les propriétés de classes.
Dans cette optique, on crée une propriété pour chaque classe à associer et le problème est résolu de lui-même.
- L'avantage est qu'il n'y a aucun problème de conflits puisque tous les composants sont isolés les uns des autres.
- L'inconvénient est que ce n'est pas uniforme ; ce n'est pas l'objet lui-même que l'on perçoit, mais des éléments séparés. Isolés, ces éléments n'ont pas de rapport entre eux, a priori.

Cette technique impose également de recourir (si l'on veut faire les choses à grande échelle) à l'injection de dépendance. C'est donc une logique qui peut être assez lourde.

#### Par l'héritage

Une seconde manière de faire est de progfiter de l'héritage multiple fourni par Python. Dans ce cas, l'approche est davntage méthodologique. On voudra s'assurer que les composants sont des bibliothèques indépendantes entre elles. une telle contrainte est, par exemple, beaucoup mieux assirée par les « traits » de langages comme PHP (sic !) ou Scala.
- L'avantage ici est que l'objet conserve son uniformité ; les méthodes des classes « sœurs » sont fusionnées ;
- L'inconvénient est qu'il s'agit d'une bonne pratique méthodologique, qui êut donc être ignorée par certains développeurs.

## Classes abstraites et interfaces

Python ne possède nativement que des _classes concrètes_. Or, pour bon nombre de raisons, il est souvent souhaitable en POO de disposer d'_interfaces_, qui servent de spécification aux classes.

Il est possible de pallier (partiellement) ce manque avec le modsule `abc`.

Grâce à `abc`, nous pouvons, au mons, définir des classes abstraites, qui nous servirons d'interfaces.

> **N.B.** Certaines classes du module `collections`, entre autres, utilisent le module `abc`

`abc` utilise les méta-classes de Python (cf. infra) pour créer une autre hiérarchie de classes.


## Introspection

Python n'est pas un langage qui a de grandes capacités d'introspection. Il n'y a pas l'équivalent, par exemple, des `ReflectionClass` de PHP. Néanmoin, il est possible d'obtenir des informations sur la structure des classes.

### Les propriétés

On peut connaître les propriétés d'une instance, et ceci de plusieurs façons. Par exemple :
```python
class A:
	def __init__:
		self.x = 10

a = A

# avec la fonction `dir`
print(dir(a))
# avec la propriété magique __dict__
print(a.__dict__)
```

### Les méthodes

On peut connaître les méthodes d'une instance ou d'une classe, et ceci de deux manières différentes :

#### Avec la fonction `dir`

```python
methods = dir(A)
```
Comme on peut le voir, le résultat est la liste de _toutes_ les méthodes, y compris les méthodes « magiques ». On doit donc purger cette liste avec une expression comme :
```python
class_methods = [m for m in dir(A) if not m.startswith('__') and callable(getattr(A, m)))]
```

#### Avec `inspect`
```python
list_of_methods = inspect.getmembers(A, predicate=inspect.isfunction)
```
Cette méthode est plus avantageuse, car elles rend une liste de tuples : les couples des noms des méthodes et de leur fonction associée.

### Autres fonctions

Parmi les fonctions classiques d'introspection, on notera :

- `isinstance`, une fonction qui permetde savoir si un objet est une instance d'une classe
- `issubclass`, une fonction qui permet de savoir si une classe est une sous-classe d'une autre.

Par ailleurs, le module `inspect` contient toute une série de fonctions utilitaires d'interrogatin des classes et des objets.

## Programmation dynamique, métaprogrammation

### Appeler dynamiquement une classe (ou une fonction)

Il est tout à fait possible pour Python d'exécuter dynamiquement une fonction. Par exemple :
```python
def f():
	return 5

def g(u):
	print(u())

g(f)
# 5
```
Mais cela marche parce que nous avons passé la fonction elle-même. Si nous avons une chaîne de caractère `'f'`, cela ne marche plus. Dans ce cas, on peut écrire :
```python
u = globals()['f']
g(u)
# 5
```

Le même mécanisme marche pour les classes :
```python
class A:
	pass

o = globals()['A']
a = o()
# <__main__.A object at 0x10bc813d0>
```

### Créer une classe dynamiquement

Il est possible de créer de nouvelles classes dynamiquement grâce à la fonction `type`.
Ordinairement, `type` permet de connaître le type d'un objet :
```python
print(type("Geeks4Geeks !"))
# --> class 'str'
print(type(1706256))
# --> class 'int'
```

Mais `type`  peut faire des choses beaucoup plus surprenantes si on lui passe plusieurs arguments :

> type(<nama>, (<super>[, <super>]+), {[<property>:<value>]* [, <method>:<callable>]*})
>
> 1. Le nom de la classe
> 2. un tuple des super-classes
> 3. un dictionaire de propriétés et de méthodes

Maintenant, il est possible d'écrire :
```python
def constructor(self, arg):
	self.constructor_arg = arg

def displayMethod(self, arg):
	print(arg)

@classmethod
def classMethod(cls, arg):
	print(arg)

# Classe
G = type("G", (object, ), {
	# Propriétés
	"string_attribute": "Geeks 4 geeks !",
	"int_attribute": 1706256,

	# Constructeur
	"__init__": constructor,

	# Méthodes
	"func_arg": displayMethod,
	"class_func": classMethod
})

# creating objects
obj = G("constructor argument")
print(obj.constructor_arg)
print(obj.string_attribute)
print(obj.int_attribute)
obj.func_arg("Geeks for Geeks")
G.class_func("Class Dynamically Created !")
```

### Utiliser ses propres méta-classes

```python
>>> class Meta(type):
...     def __new__(cls, name, bases, dct):
...         x = super().__new__(cls, name, bases, dct)
...         x.attr = 100
...         return x
...
```

> cf. [Python Metaclasses](https://realpython.com/python-metaclasses/#type-and-class)
