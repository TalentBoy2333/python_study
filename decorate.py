def drct(fun):
    def display():
        print('start')
        fun()
        print('end')
    return display

@drct
def fun():
    for i in range(10):
        print(i)

fun()