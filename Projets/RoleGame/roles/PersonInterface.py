import abc

class PersonInterface (metaclass=abc.ABCMeta):
  
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'move') and callable(subclass.move))

    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplementedError

    @abc.abstractmethod
    def move(self, x: int, y: int):
        raise NotImplementedError


