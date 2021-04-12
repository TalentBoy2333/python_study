''' 外观模式 
''' 
class CPU: 
    def run(self): 
        print('cpu run')

    def stop(self): 
        print('cpu stop')

class Disk: 
    def run(self): 
        print('disk run')

    def stop(self): 
        print('disk stop')

class Memory: 
    def run(self): 
        print('memory run')

    def stop(self): 
        print('memory stop')

class Computer: 
    def __init__(self): 
        self.cpu = CPU() 
        self.disk = Disk() 
        self.memory = Memory() 

    def run(self):
        self.cpu.run() 
        self.disk.run() 
        self.memory.run() 
    
    def stop(self): 
        self.cpu.stop() 
        self.disk.stop() 
        self.memory.stop() 


computer = Computer() 
computer.run() 
computer.stop() 