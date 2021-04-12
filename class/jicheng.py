class Animal:

    def eat(self):
        print("吃!")

    def drink(self):
        print("喝!")

    def run(self):
        print("跑!")

    def sleep(self):
        print("睡")


class Dog(Animal):  # 继承直接加上括号，不需要extends 关键字

    def bark(self):
        print("汪汪汪!")


class XiaoTianQuan(Dog):  # 继承可以传递，既继承了Animal也继承了Dog

    def fly(self):
        print("飞!")

    def bark(self):  # 重写方法
        super().bark()
        print("嗷嗷嗷!")

ahuang = XiaoTianQuan()
ahuang.bark()