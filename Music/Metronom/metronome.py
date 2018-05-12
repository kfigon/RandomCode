import winsound
import time

bpm = int(input('podaj BMP: '))
doIluLiczyc = int(input('podaj do ilu liczyc: '))
i = 0
while True:
    if i % doIluLiczyc==0:
        winsound.Beep(4000,100)
    else:
        winsound.Beep(1000,100)
    time.sleep(60/bpm)
    i +=1
