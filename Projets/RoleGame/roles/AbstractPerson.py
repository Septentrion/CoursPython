class AbstractPerson:
    """
    Classe contenant les propriétés et les comportements génériques
    de tous les personnages

    N.B. : 
        - Les noms externes des propriétés sont distinctes des noms internes.
        - Ceux-ci ne sont pas accessibles publiquement, en théorie, mais peuvent l'être en réalité.
    """

    """
    Propriétés obligatoires à l'instanciation
    """
    @property
    def name(self):
        """Accesseur de la propriété _name"""

        return self._name

    @name.setter
    def name(self, name):
        """Mutateur de la propriété _name"""

        self._name = name
        return self

    @property
    def position(self):
        """Accesseur de la propriété _position"""

        return self._position

    @position.setter
    def position(self, position):
        """Mutateur de la propriété _position"""

        # Vérification que la position est bien un tuple constitué de deux entiers
        if type(position) == tuple and type(position[0]) == int and type(position[1]) == int:
            self._position = position

    """
    Propriétés optionnelles à l'instanciation
    """
    @property
    def experience(self):
        """Accesseur de la propriété _experience"""

        if not hasattr(self, '_experience'):
            self._experience = 0
        
        return self._experience

    @experience.setter
    def experience(self, amount):
        """Mutateur de la propriété _experience"""

        self._experience = amount

    @property
    def money(self):
        """Accesseur de la propriété _money"""

        if not hasattr(self, '_money'):
            self._money = 0
        
        return self._money

    @money.setter
    def money(self, amount):
        """Mutateur de la propriété _money"""

        self._money = amount

    @property
    def objects(self):
        """Accesseur de la propriété _objects"""

        if not hasattr(self, '_objects'):
            self._objects = []

        return self._objects

    @objects.setter
    def objects(self, object):
        """Mutateur de la propriété _objects"""

        self._objects = [object]

    @property
    def weapons(self):
        """Accesseur de la propriété _weapons
        
        Liste des armes détenues par un personnage
        """

        if not hasattr(self, '_weapons'):
            self._weapons = []

        return self._weapons

    @weapons.setter
    def weapons(self, weapon):
        """Mutateur de la propriété _weapons
        
        Initialise la liste des armes avec une arme particulière
        """

        self._weapons = [weapon]

    def move(self, x: int, y: int):
        """Déplacement du personnage
        
        Il s'agit d'un déplacement unitaire et non d'un trajet

        Paramètres
        ----------
        x: int
            Le déplacement sur l'axe des abscisses
        y: int
            Le déplacement sur l'axe des ordonnées

        Returns
        -------
        self: Person
            Le personnage lui-même
        """

        pass

    def take(self, o):
        """Récolte d'un objet"""
        self.objects.append(o)

