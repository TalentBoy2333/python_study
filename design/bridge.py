''' 桥模式
''' 
from abc import ABCMeta, abstractclassmethod 

class Shape(metaclass=ABCMeta): 
    def __init__(self, color): 
        self.color = color 

    @abstractclassmethod
    def draw(self): 
        pass 

class Color(metaclass=ABCMeta): 
    @abstractclassmethod
    def paint(self, shape): 
        pass 

class Rectangle(Shape): 
    name = 'rectangle'
    def draw(self): 
        self.color.paint(self)

class Circle(Shape): 
    name = 'circle'
    def draw(self): 
        self.color.paint(self)

class Red(Color): 
    def paint(self, shape): 
        print('red {}'.format(shape.name))

class Blue(Color): 
    def paint(self, shape): 
        print('blue {}'.format(shape.name))

red_rect = Rectangle(Red())
red_rect.draw()
        