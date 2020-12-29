from typing import List, Dict, Tuple
import unittest

def find(toFind: int, occurences: Dict[int,int]) -> int:
    if toFind in occurences:
        return occurences[toFind]
    return 0

def buildDict(data: List[int]) -> Dict[int, int]:
    occurences : Dict[int, int] = {}
    for d in data:
        if d < 0 or d > 9:
            return {}
        elif d in occurences:
            occurences[d] += 1
        else:
            occurences[d] = 1
    return occurences

def findHourCombination(first: int, possibleOthers: List[int], occurences: Dict[int,int]) -> List[int]:
    if find(first, occurences) > 0:
        for i in possibleOthers:
            if i not in occurences:
                continue
            if (i != first) or (i == first and find(first, occurences) > 1):
                return [first, i]
    return []

def parse(data : List[int]) -> str:
    if len(data) != 4:
        return "0"

    occurences : Dict[int, int] = buildDict(data)
    if len(occurences) == 0:
        return "0"


    possibleHourCombinations=[
        (2,  [3,2,1,0]),
        (1,  [9,8,7,6,5,4,3,2,1,0]),
        (0,  [9,8,7,6,5,4,3,2,1,0])]
    hour = None
    for comb in possibleHourCombinations:
        res = findHourCombination(comb[0], comb[1], occurences)
        if len(res) == 2:
            hour = str(res[0]) + str(res[1])
            occurences[res[0]] -= 1
            occurences[res[1]] -= 1
            break
    if hour is None:
        return "0"


    foundMinutes = None
    for i in [5,4,3,2,1,0]:
        foundOccurences = find(i, occurences)
        if foundOccurences > 0:
            foundMinutes = i
            occurences[i] -= 1
            break
    if foundMinutes is None:
        return "0"
    

    rest = None
    for key in occurences:
        if occurences[key] > 0:
            rest = key
            occurences[key] -= 1
            break
    if rest is None:
        return "0"
    
    minutes = str(foundMinutes) + str(rest)
    return f'{hour}:{minutes}'


class TestFoo(unittest.TestCase):
    def test1(self):
        cases = [
            ([0,0,0,0], "00:00"),
            ([1,2,3,4], "23:41"),
            ([2,2,2,2], "22:22"),
            ([2,3,1,3], "23:31"),
            ([1,9,2,1], "21:19"),
            ([1,8,3,1], "18:31"),
            ([1,8,3,2], "23:18"),
            ([1,9,5,2], "21:59"),
            ([4,2,1,3], "23:41"),
            ([4,2,1,1], "21:41"),
            ([5,2,1,8], "21:58"),
            ([3,9,5,4], "0"),
            ([], "0"),
            ([1,2], "0"),
            ([4,3,7,3], "0"),
        ]
        for c in cases:
            with self.subTest(name=f'{c[0]} -> {c[1]}'):
                self.assertEqual(c[1], parse(c[0]))

if __name__ == "__main__":
    unittest.main()
