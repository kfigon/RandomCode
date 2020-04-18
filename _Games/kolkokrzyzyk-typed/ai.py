from typing import List
import random
from app import TicTacToe

class BaseOpponentStrategy:
    def doAction(self, game: TicTacToe) -> int:
        raise Exception('Not implemented')


class RandomOpponentStrategy(BaseOpponentStrategy):
    def doAction(self, game: TicTacToe)  -> int:
        emptyFieldIdxs: List[int] = game.getFreeFieldsIdxs()
        if len(emptyFieldIdxs) == 1:
            return emptyFieldIdxs[0]

        idxOfAction: int = random.randint(0,len(emptyFieldIdxs)-1)
        return emptyFieldIdxs[idxOfAction]