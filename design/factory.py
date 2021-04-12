''' 工厂模式
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


class PaymentFactory(metaclass=ABCMeta): 
    @abstractmethod
    def create_payment(self, ): 
        pass 

class AlipayFactory(PaymentFactory): 
    def create_payment(self):
        return Alipay() 

class WechatPayFactory(PaymentFactory): 
    def create_payment(self):
        return WechatPay()

class HuabeiFactory(PaymentFactory): 
    def create_payment(self):
        return Alipay(use_huabei=True)

pf = HuabeiFactory() 
p = pf.create_payment()
p.pay(100)