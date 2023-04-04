# https://www.hackerrank.com/challenges/magic-square-forming/problem
from typing import List

# all possible 3x3 magic squares
lookup: List[List[List[int]]] = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]

def createMagicSquare(matrix: List[List[int]]) -> int:
    minCost = None
    for case in lookup:
        res = calcChangeCost(case, matrix)
        if minCost is None:
            minCost = res
        minCost = min(minCost, res)

    return minCost


def calcChangeCost(case: List[List[int]], matrix: List[List[int]]) -> int:
    cost = 0
    for r in range(len(case)):
        for c in range(len(case[r])):
            ideal = case[r][c]
            provided = matrix[r][c]
            cost += abs(provided- ideal)
    return cost