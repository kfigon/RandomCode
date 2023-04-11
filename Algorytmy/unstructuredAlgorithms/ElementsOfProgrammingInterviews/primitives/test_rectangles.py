import unittest
import math
import dataclasses
from typing import Optional

@dataclasses.dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int

def intersects(r1: Rectangle, r2: Rectangle) -> Optional[Rectangle]:
    def does() -> bool:
        return (r1.x <= r2.x + r2.width and 
                r1.x + r1.width >= r2.x and
                r1.y <= r2.y + r2.height and
                r1.y + r1.height >= r2.y)

    
    if not does():
        return None
    return Rectangle(
        x=max(r1.x,r2.x),
        y=max(r1.y, r2.y),
        width=min(r1.x + r1.width, r2.x+r2.width) - max(r1.x,r2.x),
        height=min(r1.y + r1.height, r2.x+r2.height) - max(r1.y,r2.y))

# check if rectangles intersect
# if yes, return their intersection rectangle
class TestRectangles(unittest.TestCase):
    def test(self):
        pass
        # (Rectangle(x=1,y=2,width=5,height=5), Rectangle(x=6,y=7,width=15,height=10), None),
        # self.assertEqual(intersects(d[0],d[1]), d[2])
        # self.assertEqual(intersects(d[1],d[0]), d[2])

if __name__ == '__main__':
    unittest.main()