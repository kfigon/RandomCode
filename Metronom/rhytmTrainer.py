import random

for takt in range(8):    
    for nuta in range(4):
            if random.randint(1,10) < 8:
                print('x ', end='')
            else:
                print('o ', end='')
    print('| ', end='')

