from roles.AbstractPerson import AbstractPerson as Person

class AbstractThief() :
    """
    Classe de voleurs.
    Leurs propriétés spécifiques sont la _visibilité_ et l'_agilité_
    Leurscomportements spécifiques sont _steal_, pour voler un autre personnage et _unlock_, pour ouvrir une serrure

    N.B. :
        - Tous les mutateurs retournent l'objet lui-même
        - Les propriétés internes sont protégées
        - Si les propriétés n'ont pas de valeur, alors on leur assigne une valeur par défaut à la première lecture
    """


    @property
    def visibility(self):
        """Accesseur de la propriété _visibility"""

        # if not hasattr(self, '_visibility'):
        #    self._visibility = 0
        
        return self._visibility

    @visibility.setter
    def visibility(self, amount):
        """Mutateur de la propriété _visibility"""
        
        self._visibility = amount

    def gainVisibility(self, amount):
        """Augmentation de la visibilité

        Parameters
        ----------
        amount: float
            Le coefficient de visibilité ajouté

        Returns
        -------
        self: Person
            Le personnage lui-même
        """
        
        self._visibility = self.visibility + amount
        return self

    def loseVisibility(self, amount):
        """Diminution de la visibilité

        Parameters
        ----------
        amount: float
            Le coefficient de visibilité retranché

        Returns
        -------
        self: Person
            Le personnage lui-même
        """
        
        self.gainvisibility(-amount)
        return self

    @property
    def agility(self):
        """Accesseur de la propriété _agility"""
        
        if not hasattr(self, '_agility'):
            self._agility = 0
        
        return self._agility

    @agility.setter
    def agility(self, amount):
        """Mutateur de la propriété _agility"""
        
        self._agility = amount

    def gainAgility(self, amount):
        """Augmentation de l'agilité

        Parameters
        ----------
        amount: float
            Le coefficient d'agilité ajouté

        Returns
        -------
        self: Person
            Le personnage lui-même
        """
        
        self._agility = self.agility + amount
        return self

    def loseAgility(self, amount):
        """Diminution de l'agilité

        Parameters
        ----------
        amount: float
            Le coefficient d'agilité retranché

        Returns
        -------
        self: Person
            Le personnage lui-même
        """
        
        self.gainAgility(-amount)
        return self

    def steal(self, other):
        """Action de voler un objet à un autre personnage

        Parameters
        ----------
        other: Person
            Le personnage qui est volé

        Returns
        -------
        self: Person
            L'auteur du vol
        """
        
        if isinstance(other, 'Person') and len(other.objects) > 0:
            index = randint(0, len(other.objects) -1)
            self.take(other.objects[index])
        return self

    def unlock(self, object):
        """Action de crocheter une serrure

        Parameters
        ----------
        object: Unlockable
            La serrure qui doit être ouverte

        Returns
        -------
        self: Person
            L'auteur du crochetage
        """
        
        if object.islockable():
            pass
        return self


