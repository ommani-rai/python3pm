from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def findarea(self):
        print("from findarea method")


class Rectangle(shape):
    def area(self):
        print('area of rectangle')

# obj = shape()
child = Rectangle()
child.area()
child.findarea()

