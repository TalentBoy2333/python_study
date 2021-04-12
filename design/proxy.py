''' 代理模式 
''' 
from abc import ABCMeta, abstractclassmethod, abstractmethod 

class Subject(metaclass=ABCMeta): 
    @abstractmethod
    def get_content(self): 
        pass 

    @abstractclassmethod
    def set_content(self, content): 
        pass 

class RealSubject(Subject): 
    def __init__(self, filename): 
        self.filename = filename 
        f = open(filename, 'r')
        print('open file')
        self.content = f.read() 
        f.close() 

    def get_content(self): 
        return self.content 
    
    def set_content(self, content): 
        f = open(self.filename, 'w')
        f.write(content)
        f.close() 

class VitualProxy(Subject): 
    def __init__(self, filename): 
        self.filename = filename 
        self.subj = None 
    
    def get_content(self): 
        if not self.subj: 
            self.subj = RealSubject(self.filename) 
        return self.subj.get_content() 

    def set_content(self, content): 
        if not self.subj: 
            self.subj = RealSubject(self.filename)  
        self.subj.set_content() 

s1 = RealSubject('test.txt') # 不调用get_content，也会将内容存在内存里

p1 = VitualProxy('test.txt') # 只有调用了get_content，才会将内容存在内存里

        
class ProtectedProxy(Subject): 
    def __init__(self, filename): 
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content() 

    def set_content(self, content): 
        raise PermissionError('no persission for write')

p2 = ProtectedProxy('test.txt')
print(p2.get_content())
p2.set_content('test') 
