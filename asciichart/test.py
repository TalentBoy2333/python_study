import asciichartpy
import numpy as np 

config = {
    "height": 20,
    "colors": [
        asciichartpy.green,
    ]
}

x = np.arange(0, 10, 0.1)
y = np.sin(x)
x = list(x)
y = list(y)
# print(x)
# print(y)


print(asciichartpy.plot([y], config))