# abstrction(추상화)
from  abc import  ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def atea(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

#a = Circle
# rectangle triangle

from abc import ABC.abstractmethod()
class Shae(ABC):
    def __init__(self):
        self.concep = concep

    def verif(self):
        @abstractmethod
        pass

class Rectangle(Shape):
    def  form(self):
        print("마주보는 두변은 같다.")
class Triangle(Shape):
    def form(self):
        print("3")
    def

class Rectangle(Shape):

class Triangle(Shape):
