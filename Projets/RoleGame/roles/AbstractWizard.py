from roles.AbstractPerson import AbstractPerson as Person

class AbstractWizard() :
    """
    Classe de magiciens.
    Leurs propriétés spécifiques sont la _mana_
    Leurs comportements spécifiques sont _spell_, pour jeter un sort

    N.B. :
        - Tous les mutateurs retournent l'objet lui-même
        - Les propriétés internes sont protégées
        - Si les propriétés n'ont pas de valeur, alors on leur assigne une valeur par défaut à la première lecture
    """

    WIZARD_SPEED = 1
    @property
    def mana(self):
        """Accesseur de la propriété _mana"""
        if not hasattr(self, '_mana'):
            self._mana = 0
        
        return self._mana

    @mana.setter
    def mana(self, amount):
        """Mutateur de la propriété _mana"""
        self._mana = amount

    def gainMana(self, amount):
        """Augmentation de mana

        Parameters
        ----------
        amount: float
            Le coefficient de mana ajouté

        Returns
        -------
        self: Person
            Le personnage lui-même
        """
        self._mana = self.mana + amount
        return self

    def loseMana(self, amount):
        """Diminution de mana

        Parameters
        ----------
        amount: float
            Le coefficient de mana retranché

        Returns
        -------
        self: Person
            Le personnage lui-même
        """
        self.gainMana(-amount)
        return self

    def spell(self, other):
        """Action de jeter un sort à un autre personnage

        Parameters
        ----------
        other: Person
            Le personnage qui est affecté par le sort

        Returns
        -------
        self: Person
            L'auteur du vol
        """
        if isinstance(other, 'Person'):
            other.loseLifes(10)
        pass

