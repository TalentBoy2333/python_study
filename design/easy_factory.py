''' 简单工厂模式
'''
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta): 

    @abstractmethod
    def pay(self, money): 
        pass

class Alipay(Payment): 
    def __init__(self, use_huabei=False): 
        self.use_huabei = use_huabei

    def pay(self, money): 
        if self.use_huabei: 
            print('huabei: {}'.format(money))
        else: 
            print('Alipay: {}'.format(money)) 

class WechatPay(Payment): 
    def pay(self, money): 
        print('Wechat: {}'.format(money)) 

class PaymentFactory: 
    def create_payment(self, method): 
        if method == 'alipay': 
            return Alipay() 
        elif method == 'wechat': 
            return WechatPay() 
        elif method == 'huabei': 
            return Alipay(use_huabei=True) 
        else: 
            raise TypeError('No such class named {}'.format(method))

pf = PaymentFactory() 
p = pf.create_payment('huabei')
p.pay(100)