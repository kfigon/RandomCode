from typing import List, Dict

# corrupted passwords v2:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

# Each policy actually describes two positions in the password, 
# where 1 means the first character, 
# 2 means the second character, and so on.
#  (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
# Exactly one of these positions must contain the given letter. 
# Other occurrences of the letter are irrelevant for the purposes of 
# policy enforcement.

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

class Data:
    def __init__(self, mini: int, maxi: int, letter: str, password: str):
        self.min = mini
        self.max = maxi
        self.letter = letter
        self.password = password

    def isCorrect(self) -> bool:
        firstMatched = self.password[self.min-1] == self.letter
        secondMatched = self.password[self.max-1] == self.letter

        return firstMatched ^ secondMatched

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

assert len(res) == 1
assert res[0].password == 'abcde'

with open('inputData.txt', 'r') as f:
    challengeInput = f.read()
    out = findCorrect(parseInput(challengeInput))
    print(len(out))
    assert len(out) == 313