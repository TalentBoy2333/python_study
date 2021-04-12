''' 抽象工厂模式
'''

from abc import ABCMeta, abstractmethod

# 抽象产品

class PhoneShell(metaclass=ABCMeta): 
    @abstractmethod
    def show_shell(self): 
        pass 

class CPU(metaclass=ABCMeta): 
    @abstractmethod
    def show_cpu(self):
        pass 

class OS(metaclass=ABCMeta): 
    @abstractmethod 
    def show_os(self): 
        pass 

# 抽象工厂

class PhoneFactory(metaclass=ABCMeta): 
    @abstractmethod
    def make_shell(self): 
        pass 

    @abstractmethod
    def make_cpu(self): 
        pass

    @abstractmethod
    def make_os(self): 
        pass

# 具体产品

class SmallShell(PhoneShell): 
    def show_shell(self): 
        print('小手机壳') 

class BigShell(PhoneShell): 
    def show_shell(self): 
        print('大手机壳') 

class AppleShell(PhoneShell): 
    def show_shell(self): 
        print('苹果手机壳') 

class SnapDragonCPU(CPU): 
    def show_cpu(self): 
        print('晓龙cpu')

class MediaTekCPU(CPU): 
    def show_cpu(self): 
        print('联发科cpu')

class AppleCPU(CPU): 
    def show_cpu(self): 
        print('苹果cpu')

class Android(OS): 
    def show_os(self): 
        print('安卓操作系统')

class IOS(OS): 
    def show_os(self): 
        print('ios操作系统')

# 具体工厂

class MiFactory(PhoneFactory): 
    def make_shell(self):
        return BigShell() 

    def make_cpu(self):     
        return SnapDragonCPU() 
    
    def make_os(self):
        return Android() 

class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

    def make_cpu(self):     
        return MediaTekCPU() 
    
    def make_os(self):  
        return Android() 

class IPhoneFactory(PhoneFactory): 
    def make_shell(self):
        return AppleShell() 

    def make_cpu(self):     
        return AppleCPU() 
    
    def make_os(self):  
        return IOS() 


# 客户端

class Phone: 
    def __init__(self, shell, cpu, os): 
        self.shell = shell 
        self.cpu = cpu 
        self.os = os 

    def show_info(self): 
        print('phone info')
        self.shell.show_shell() 
        self.cpu.show_cpu() 
        self.os.show_os() 


def make_phone(factory):
    shell = factory.make_shell() 
    cpu = factory.make_cpu() 
    os = factory.make_os() 
    return Phone(shell, cpu, os)

p1 = make_phone(IPhoneFactory())
p1.show_info()




        