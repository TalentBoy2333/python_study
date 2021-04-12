''' 接口实现
'''
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta): 

    @abstractmethod
    def pay(self, money): 
        pass

class Alipay(Payment): 
    def pay(self, money): 
        print('Alipay: {}'.format(money)) 

class WechatPay(Payment): 
    def pay(self, money): 
        print('Wechat: {}'.format(money)) 

p = Alipay() 
p.pay(100)
p = WechatPay() 
p.pay(200)