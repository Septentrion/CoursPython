from random import randint

from roles.AbstractWizard import AbstractWizard
from roles.AbstractThief import AbstractThief
from roles.AbstractPerson import AbstractPerson
from roles.PersonInterface import PersonInterface

class WarriorThief (AbstractThief, AbstractPerson, PersonInterface):

    def __init__(self, name):
        self._name = name
        self._position = (randint(0,100),randint(0,100))
