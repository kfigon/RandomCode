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

    def __repr__(self):
        return f'({self.x},{self.y})'
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def sortingFunction(lowest: Point, a: Point) -> float:
    return math.atan2((a.y-lowest.y), (a.x-lowest.x))

# is c to the left of ray a->b
# a->b->c
def isCounterClockwise(a: Point, b: Point,c: Point) -> bool:
    res: int = (b.x - a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)
    # res < 0 - clockwise, >0 counter, == 0 - collinear
    return res > 0

# https://algorithmtutor.com/Computational-Geometry/Convex-Hull-Algorithms-Graham-Scan/
class GrahamScan:
    def __init__(self, points: List[Point]):
        self.points = points

    def findSmallest(self) -> Point:
        smallest = None
        for i in self.points:
            if smallest is None:
                smallest = i
            elif(i.y < smallest.y):
                smallest = i
            elif (i.y == smallest.y and i.x < smallest.x):
                smallest = i
        return smallest

    def generate(self) -> List[Point]:
        if len(self.points) <= 3:
            return self.points

        lowest = self.findSmallest()
        self.points.sort(key=lambda p: sortingFunction(lowest, p))

        hull: List[Point] = [lowest, self.points[0]]

        for i in range(2, len(self.points)):
            currentPoint = self.points[i]
            top = hull.pop()
            lastEntry = hull[-1]
            while not isCounterClockwise(lastEntry, top, currentPoint):
                top = hull.pop()
                lastEntry = hull[-1]

            hull.append(top)
            hull.append(currentPoint)
        
        return hull

def parseInput(string : str) -> List[Point]:
    splittedLines = map(lambda line: line.split(' '), string.strip().splitlines())
    return list(map(lambda vals: Point(int(vals[0]), int(vals[1])), splittedLines))

if __name__ == "__main__":        
    inputString = '''7 0
1 4
3 1 
3 3 
5 2
5 5
0 0
9 6'''

    points: List[Point] = parseInput(inputString)
    gs = GrahamScan(points)
    print(gs.generate())
