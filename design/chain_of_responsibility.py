''' 责任链模式
''' 
from abc import ABCMeta, abstractclassmethod, abstractmethod 

class Handler(metaclass=ABCMeta): 
    @abstractmethod
    def handle_leave(self, day): 
        pass 

class GeneralManager(Handler): 
    def handle_leave(self, day):
        if day <= 10: 
            print('GeneralManager handle {} day'.format(day))
        else: 
            print('you fired!')

class DepartmentManager(Handler): 
    def __init__(self): 
        self.next = GeneralManager() 

    def handle_leave(self, day):
        if day <= 5: 
            print('DepartmentManager handle {} day'.format(day))
        else: 
            print('DepartmentManager has no assess for {} day'.format(day))
            self.next.handle_leave(day)

class ProjectDector(Handler): 
    def __init__(self): 
        self.next = DepartmentManager() 

    def handle_leave(self, day):
        if day <= 3: 
            print('ProjectDector handle {} day'.format(day))
        else: 
            print('ProjectDector has no assess for {} day'.format(day))
            self.next.handle_leave(day)

h = ProjectDector() 
h.handle_leave(2)
print()

h.handle_leave(4)
print()

h.handle_leave(6)
print()

h.handle_leave(12)