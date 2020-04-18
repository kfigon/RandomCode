from typing import List, Callable
from enum import Enum
import logging

class Field(Enum):
    EMPTY = 0
    X = 1
    O = 2

class GameResult(Enum):
    PENDING = 0
    X_WIN = 1
    O_WIN = 2
    TIE = 3

class TicTacToe:
    def __init__(self):
        self.gameArea :List[Field] = [Field.EMPTY for _ in range(9)]
        self.currentPlayer: Field = Field.X

    # 0 1 2
    # 3 4 5
    # 6 7 8
    def getStatus(self) -> GameResult:
        if self.__doesPlayerWon(Field.X):
            return GameResult.X_WIN
        elif self.__doesPlayerWon(Field.O):
            return GameResult.O_WIN
        elif self.__anyEmptyPlace():
            return GameResult.PENDING
        return GameResult.TIE

    def __anyEmptyPlace(self) -> bool:
        for f in self.gameArea:
            if f == Field.EMPTY:
                return True
        return False

    def __doesPlayerWon(self, player :Field) -> bool:
        g = self.gameArea
        
        isHorisontalWin :Callable[[int], bool] = lambda row: g[3*row] == player and g[3*row+1] == player and g[3*row+2] == player
        isVerticalWin :Callable[[int], bool] = lambda col: g[col] == player and g[col+3] == player and g[col+6] == player
        
        for i in range(3):
            if isHorisontalWin(i) or isVerticalWin(i):
                return True

        if (g[0] == player and g[4] == player and g[8] == player) or (g[2] == player and g[4] == player and g[6] == player):
            return True
        
        return False

    def move(self, position: int) -> None:
        if position < 0 or position >= len(self.gameArea):
            raise ValueError(f'Invalid move to {position}')
        elif self.gameArea[position] != Field.EMPTY:
            raise ValueError(f'Invalid move to {position}, field is taken by {self.gameArea[position]}')

        logging.info(f'moving {self.currentPlayer} to {position}')
        self.gameArea[position] = self.currentPlayer
        self.__changePlayer()
               
    def __changePlayer(self) -> None:
        if self.currentPlayer == Field.X:
            self.currentPlayer = Field.O
        else:
            self.currentPlayer = Field.X
    
    def getFreeFieldsIdxs(self) -> List[int]:
        emptyFieldIdxs : List[int]= []
        for idx, f in enumerate(self.gameArea):
            if f == Field.EMPTY:
                emptyFieldIdxs.append(idx)
        return emptyFieldIdxs

    def __str__(self) -> str:
        out = ''
        
        for idx, field in enumerate(self.gameArea):
            if idx != 0 and idx % 3 == 0:
                out += '\n'

            if field == Field.X:
                out += 'X'
            elif field == Field.O:
                out += 'O'
            else:
                out += str(idx)

        return out

        