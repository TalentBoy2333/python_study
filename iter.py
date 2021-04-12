# 生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

for i in fib(10):
    print(i)

# 迭代器
t = iter([1,2,3,4])
print(t.__next__())
for i in t:
    print(t)