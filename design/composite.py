''' 组合模式
''' 
from abc import ABCMeta, abstractclassmethod 

class Graghic(metaclass=ABCMeta): 
    @abstractclassmethod
    def draw(self): 
        pass 

class Point(Graghic): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

    def __str__(self): 
        return 'point({}, {})'.format(self.x, self.y)
    
    def draw(self):
        print(str(self)) 

class Line(Graghic): 
    def __init__(self, p1, p2): 
        self.p1 = p1 
        self.p2 = p2 
    
    def __str__(self): 
        return 'line[{}, {}]'.format(self.p1, self.p2)

    def draw(self): 
        print(str(self))

class Picture(Graghic): 
    def __init__(self, iterable): 
        self.graghic = [] 
        for g in iterable: 
            self.add(g)
    
    def add(self, g): 
        self.graghic.append(g)

    def draw(self): 
        print('Picture')
        for g in self.graghic: 
            g.draw()
        print('Picture')
        

p1 = Point(1, 1)
line1 = Line((2, 2), (3, 3))
pic1 = Picture([p1, line1])

p2 = Point(4, 4)
line2 = Line((5, 5), (6, 6))
pic2 = Picture([p2, line2])

pic = Picture([pic1, pic2])
pic.draw() 