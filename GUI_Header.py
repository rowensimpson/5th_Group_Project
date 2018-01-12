import random
from time import sleep

open('sampleText2.txt', 'w').close()
index = 0

stateindex = ['reset', 'export', 'import', 'error']
state1 = 'reset'
state2 = 'reset'
state3 = 'reset'

while True:
    afile = open("sampleText2.txt", "a")
    afile.write(str(index))
    index = index + 1
    for i1 in range(12):
        afile.write(',')
        line = str(random.randint(0, 50))
        afile.write(line)
        #print(line)
    if index%10 == 0:
        state1 = str(stateindex[random.randint(0, 3)])
        state2 = str(stateindex[random.randint(0, 3)])
        state3 = str(stateindex[random.randint(0, 3)])
    final = ',' + state1 + ',' + state2 + ',' + state3
    afile.write(final)
    #print(final)
    afile.write('\n\r')
    afile.close()
    sleep(0.5)


