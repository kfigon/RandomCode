import winsound
import time

bpm = int(input('podaj BMP: '))
i = 0
while True:
    if i % 4==0:
        winsound.Beep(4000,100)
    else:
        winsound.Beep(1000,100)
    time.sleep(60/bpm)
    i +=1
