#!/usr/bin/env python3

import asciichartpy
import random
from time import sleep

S1 = [random.randint(-100, -25) for x in range(1, 60)]
S2 = [random.randint(-25, 50) for x in range(1, 60)]
S3 = [random.randint(25, 100) for x in range(1, 60)]

while True:

    print("\033[H\033[J", end='') # clear screen

    config = {
        "height": 20,
        "colors": [
            asciichartpy.green,
            asciichartpy.blue,
            asciichartpy.red
        ]
    }

    for i in range(0, len(S1)-1):
        S1[i] = S1[i+1]
    S1[-1] = random.randint(-100, 0)

    for i in range(0, len(S2)-1):
        S2[i] = S2[i+1]
    S2[-1] = random.randint(-50, 50)

    for i in range(0, len(S3)-1):
        S3[i] = S3[i+1]
    S3[-1] = random.randint(0, 100)

    print(asciichartpy.plot([S1, S2, S3], config))
    sleep(1)