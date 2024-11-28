from abc import ABC, abstractmethod

class Fruints(ABC):
    @abstractmethod
    def quantity(self):
        raise NotImplementedError
    
class Banana(Fruints):
    def quantity(self):
        print("This is quantity Banana")

class Apple(Fruints):
    def quantity(self):
        print("This is quantity Apple")

bn: Fruints = Banana()
bn.quantity()