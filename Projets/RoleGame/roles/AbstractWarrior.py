class AbstractWarrior() :
    """
    Classe de guerriers.
    Leur propriété spécifique est la _rage_
    Ils ont un comportement spécifique _berserk_

    N.B. :
        - Tous les mutateurs retournent l'objet lui-même
        - Les propriétés internes sont protégées
    """
   

    @property
    def rage(self):
        """Accesseur de la propriété _rage"""

        if not hasattr(self, '_rage'):
            self._rage = 0
        
        return self._rage

    @rage.setter
    def rage(self, amount):
        """Mutateur de la propriété _rage"""

        self._rage = amount

    def gainRage(self, amount):
        """Augmentation de la rage d'une certaine quantité

        Parameters
        ----------
        amount: float
            Le coefficient de rage ajouté

        Returns
        -------
        self: Person
            Le personnage lui-même
        """
        
        self._rage = self.rage + amount
        return self

    def loseRage(self, amount):
        """
        Diminution de la rage d'une certaine quantité

        Parameters
        ----------
        amount: float
            Le coefficient de rage retranché

        Returns
        -------
        self: Person
            Le personnage lui-même
        """
        
        self.gainRage(-amount)
        return self

    def berserk(self):
        """Berserk ? """
            pass

