from dataclasses import dataclass
from typing import List
from operator import attrgetter
import math

@dataclass
class Point:
    x: int
    y: int

def angle(a: Point, b: Point) -> float:
    return math.atan2((b.y-a.y)/(b.x-a.x))


class GrahamScan:
    def __init__(self, points: List[Point]):
        self.points = points

    def generate(self) -> List[Point]:
        lowest = min(self.points, key=attrgetter('y'))
        self.points.sort(key=lambda p: angle(p, lowest))
        hull: List[Point] = [lowest]
        for p in self.points:
            pass
        return hull
        