''' 策略模式 
''' 
from abc import ABCMeta, abstractclassmethod 

class Strategy(metaclass=ABCMeta): 
    @abstractclassmethod 
    def execute(self, data): 
        pass 

class FastStrategy(Strategy): 
    def execute(self, data): 
        print('fast method:', data)

class SlowStrategy(Strategy): 
    def execute(self, data): 
        print('slow method:', data) 

class Context: 
    def __init__(self, strategy, data): 
        self.data = data 
        self.strategy = strategy 
    
    def set_strategy(self, strategy): 
        self.strategy = strategy 

    def do_strategy(self): 
        self.strategy.execute(self.data) 

data = '***' 
s1 = FastStrategy() 
s2 = SlowStrategy()

context = Context(s1, data) 
context.do_strategy() 

context.set_strategy(s2) 
context.do_strategy() 
