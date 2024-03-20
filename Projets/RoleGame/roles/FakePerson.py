class FakePerson :

    def __init__(self, name):
        self._name = name
        self._position = (randint(0,100),randint(0,100))

    def move(self, x, y, z):
        pass
