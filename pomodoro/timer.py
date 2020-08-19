from dataclasses import dataclass
from os import system
import time

@dataclass
class TimerData:
    workTime: int
    shortBreakTime: int
    longBrakeTIme: int
    numerOfShortRounds: int

class Timer:
    def __init__(self, timerData: TimerData):
        self.data = timerData
        self.stateMachine = StateMachine(timerData.numerOfShortRounds)

    def getTimerForState(self):
            if self.stateMachine.currentState == StateMachine.WORK:
                return self.data.workTime
            elif self.stateMachine.currentState == StateMachine.SHORT:
                return self.data.shortBreakTime
            return self.data.longBrakeTIme

    def wait(self, secondsToWait: int):
        seconds: int = 0
        allTime = secondsToWait//60, secondsToWait%60
        while seconds <= secondsToWait:
            currentTime = seconds//60, seconds%60
            print(f'{currentTime[0]}:{currentTime[1]} / {allTime[0]}:{allTime[1]}', end='\r')
            seconds+=1
            time.sleep(1)

    def run(self):
        while True:
            system('cls')
            time = self.getTimerForState()
            print(f'{self.stateMachine.currentState}')
            self.wait(time)
            self.stateMachine.nextState()

class StateMachine:
    WORK : str = 'work'
    SHORT: str = 'short'
    LONG: str = 'long'

    def __init__(self, numerOfShortRounds: int):
        self.numerOfShortRounds = numerOfShortRounds
        self.currentState: str = StateMachine.WORK
        self.currentRound: int = 0
    
    def nextState(self):
        if self.currentState == StateMachine.WORK:
            if self.currentRound < self.numerOfShortRounds:
                self.currentState = StateMachine.SHORT
                self.currentRound +=1
            else:
                self.currentState = StateMachine.LONG
                self.currentRound = 0
        else:
            self.currentState = StateMachine.WORK


t = Timer(TimerData(30,5,10,2))
t.run()