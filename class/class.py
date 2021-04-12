class Tool(object):
    count = 0  # 这个是类属性, 一般在这个位置定义

    # 不需要访问任何属性或使用方法, 定义静态方法
    @staticmethod
    def run():  # 注意这里第一个参数不需要self或者cls
        print("运行...")
    
    @classmethod
    def show_tool_count(cls):  # 类方法
        print("工具对象的数量 %d " % cls.count)   # 这个和self类似，取的是类内部的属性和方法

    def __init__(self, name):
        self.name = name # 对象属性
        Tool.count += 1  # 统计创建了多少个实例方法


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
print(Tool.count)  # 3
# 也可以查看对象的count属性　-- > 属性的获取机制
print(tool3.count)  # 3

Tool.show_tool_count()  # 3
Tool.run()