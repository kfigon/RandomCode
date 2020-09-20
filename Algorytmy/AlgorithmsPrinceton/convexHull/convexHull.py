from dataclasses import dataclass
from typing import List
from operator import attrgetter
import math

# https://www.coursera.org/learn/algorithms-part1/lecture/KHJ1t/convex-hull
# https://pl.wikipedia.org/wiki/Algorytm_Grahama

@dataclass
class Point:
    x: int
    y: int

def angle(a: Point, b: Point) -> float:
    return math.atan2((b.y-a.y), (b.x-a.x))

# is c to the left of ray a->b
# a->b->c
def isCounterClockwise(a: Point, b: Point,c: Point) -> bool:
    res = (b.x - a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)
    # res < 0 - clockwise, >0 counter, == 0 - collinear
    return res > 0

class GrahamScan:
    def __init__(self, points: List[Point]):
        self.points = points

    def generate(self) -> List[Point]:
        lowest = min(self.points, key=attrgetter('y'))
        self.points.sort(key=lambda p: angle(p, lowest))
        hull: List[Point] = [lowest, self.points[0]]

        for i in range(2, len(self.points)):
            currentPoint = self.points[i]
            top = hull.pop()
            lastEntry = hull[-1]
            while not isCounterClockwise(lastEntry, top, currentPoint):
                top = hull.pop()
            hull.append(top)
            hull.append(currentPoint)
        
        return hull

def parseInput(string : str) -> List[Point]:
    splittedLines = map(lambda line: line.split(' '), string.splitlines())
    return list(map(lambda vals: Point(int(vals[0]), int(vals[1])), splittedLines))

if __name__ == "__main__":        
    inputString = '''1 1
4 4
5 3
6 4'''

    points: List[Point] = parseInput(inputString)
    gs = GrahamScan(points)
    #  zle!
    print(gs.generate())
