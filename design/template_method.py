''' 模板方法模式
''' 
from abc import ABCMeta, abstractclassmethod 
from time import sleep

class Window(metaclass=ABCMeta): 
    @abstractclassmethod 
    def start(self): 
        pass 

    @abstractclassmethod 
    def repaint(self): 
        pass 

    @abstractclassmethod 
    def stop(self): 
        pass 

    def run(self):  # 模板方法
        self.start() 
        while True: 
            try: 
                self.repaint() 
                sleep(1)
            except KeyboardInterrupt: 
                break 

        self.stop() 

class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg 

    def start(self): 
        print('start')

    def stop(self): 
        print('stop')

    def repaint(self): 
        print(self.msg) 

MyWindow('hello').run()



