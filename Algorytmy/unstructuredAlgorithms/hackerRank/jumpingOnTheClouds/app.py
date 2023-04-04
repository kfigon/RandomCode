# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
from typing import List

def isThunder(cloud: int) -> bool:
    return cloud == 1

def countJumps(clouds: List[int]) -> int:
    jumps = 0
    i = 0
    while i < len(clouds)-2:
        nextCloud = clouds[i+1]
        nextNextCloud = clouds[i+2]
        if isThunder(nextCloud) or not isThunder(nextNextCloud):
            i += 2
        else:
            i +=1
        jumps += 1

    # last missing jump
    if i != len(clouds)-1:
        jumps+=1
    return jumps

assert countJumps([0,1,0,0,0,1,0]) == 3
assert countJumps([0,0,1,0,0,1,0]) == 4
assert countJumps([0,0,0,1,0,0]) == 3
print('oks')