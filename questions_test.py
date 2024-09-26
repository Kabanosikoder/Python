from random import randint
import random
from math import floor


print(floor(-2.2))  # floor rounds down

for i in range(100):
    randnum = randint(1, 6)
    print(randnum)

for i in range(100):
    random_stuff = (random.randint(0, 4) - 2) * 2
    print(random_stuff)