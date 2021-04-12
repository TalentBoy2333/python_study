''' 适配器模型
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

class BankPay: 
    def cost(self, money): 
        print('Bank: {}'.format(money))

# # 类适配器
# class NewBankPay(Payment, BankPay): 
#     def pay(self, money): 
#         self.cost(money)

# p = NewBankPay() 
# p.pay(100)

# 对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment): 
        self.payment = payment 

    def pay(self, money): 
        self.payment.cost(money)

p = PaymentAdapter(BankPay()) 
p.pay(100)

