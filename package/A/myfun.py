from .fun import add

def myadd(a,b,c):
    return add(add(a,b),c)

'''
该路径下无法运行
若要运行，可以使用如下方法：
if __name__ == '__main__':
    from fun import add
else:
    from .fun import add
'''
if __name__ == '__main__':
    print(myadd(1, 2, 3))