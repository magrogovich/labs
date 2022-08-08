from random import*
import time


test = True
while test == True:
    x = randrange(0, 100)
    y = randrange(0, 100)
    with open("coordinates.txt", "w") as data:
        data.write(f"{x},{y}\n")
    time.sleep(10)



