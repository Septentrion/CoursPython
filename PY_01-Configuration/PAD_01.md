# Installation et configuration de Python

## Installation



## Environnements virtuels

Il est possible de créer des « environnemments virtuels », c'est-aà-dire des conteneurs isolés, dans lesquels il sera possible d'installer des versins spécifiques de Python ou de modules divers. Cela est possible dans n'importe qul dossier du système pouvu que Python soit installe globalement.

La procédure est très simple :
```python
# Créer l'environnement
python -m venv .venv
```

> Cela signifie : Exécute le module (`-m`) `venv` et crée un dossier `.venv`. Le nom de ce dossier est arbitraire, mais `venv` ou `.venv` (le caractère `.` désignat le fait que c'est un dossier de configuration) est une convention pertinente.

Deuxième étape, il faiut activer l'environnement virtuel, sans quoi l'on restera attaché à la verszion globale de Python.
```python
# Activation
. .venv/bin/activate
```

> Attention le premier point est une commande et l'espace entre les deux points n'est pas une erreur !
> Vous remarquerez que l'invite du shell change pour indiquer que vous êtes entrés dans le nouvel environnement.

Maintenant, vous pouvez installer les modules dont vous avez besoin :
```python
# Installation de Flask, par exemple
pip install flask
```

Si vous voulez quitter l'environnement virtuel, il suffit d'exécuter :
```python
deactivate
```


