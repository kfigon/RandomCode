from typing import List, Dict

# corrupted passwords:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

# Each line gives the password policy and then the password. 
# The password policy indicates the lowest and highest number 
# of times a given letter must appear for 
# the password to be valid. 

# For example, 1-3 a means that the password must contain a at 
# least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. 
# The middle password, cdefg, is not; 
# it contains no instances of b, but needs at least 1. 
# The first and third passwords are valid: 
# they contain one a or nine c, both within the limits 
# of their respective policies.

class Data:
    def __init__(self, mini: int, maxi: int, letter: str, password: str):
        self.min = mini
        self.max = maxi
        self.letter = letter
        self.password = password

    def isCorrect(self) -> bool:
        occurences: Dict[str, int] = {}
        for i in self.password:
            if i == self.letter:
                if i in occurences:
                    occurences[i] += 1
                else:
                    occurences[i] = 1
        return self.letter in occurences and  occurences[self.letter] >= self.min and  occurences[self.letter] <= self.max

    def __str__(self) -> str:
        return f'{self.min}-{self.max} {self.letter}: {self.password}'

def findCorrect(data: List[Data]) -> List[Data]:
    return list(filter(lambda x: x.isCorrect(), data))

def parseLine(line: str) -> Data:
    parts = line.split(' ')
    mini, maxi = parts[0].split('-')
    letter = parts[1].replace(':', '')
    password = parts[2]
    return Data(int(mini), int(maxi), letter, password)

def parseInput(inputStr: str) -> List[Data]:
    return list(map(parseLine, inputStr.splitlines()))

inp = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''

d = parseInput(inp)
res = findCorrect(d)

assert len(res) == 2
assert res[0].password == 'abcde'
assert res[1].password == 'ccccccccc'

with open('inputData.txt', 'r') as f:
    challengeInput = f.read()
    out = findCorrect(parseInput(challengeInput))
    print(len(out))
    assert len(out) == 500