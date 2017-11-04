# code used to test the GUI by flooding in data

import random
from time import sleep

open('sampleText2.txt', 'w').close()

for i in range(int(input("how much data?: "))):
    afile = open("sampleText2.txt", "a")
    afile.write(str(i))
    for i1 in range(12):
        afile.write(',')
        line = str(random.randint(0, 50))
        afile.write(line)
        print(line)
    afile.write('\n')
    afile.close()
    sleep(0.5)


