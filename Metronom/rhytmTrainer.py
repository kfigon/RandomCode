import random
import winsound
import time

def bang():
    x = random.randint(1,10)
    return x<8

for takt in range(8):    
    for nuta in range(4):
            if bang():
                print('x ', end='')
            else:
                print('o ', end='')
    print('| ', end='')


bpm = 30
i = 0
while True:
    if i % 4==0:
        winsound.Beep(4000,100)
    else:
        winsound.Beep(1000,100)
    time.sleep(60/bpm)
    i +=1
