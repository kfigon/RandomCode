from typing import List, Tuple

# Your plane lands with plenty of time to spare. The final leg of your journey is a ferry
#  that goes directly to the tropical island where you can finally start your vacation.
#   As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

# By modeling the process people use to choose (or abandon) their seat in the waiting 
# area, you're pretty sure you can predict the best place to sit. You make a 
# quick map of the seat layout (your puzzle input).

# The seat layout fits neatly on a grid. Each position is either floor (.), an 
# empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

first='''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

# Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely
#  predictable and always follow a simple set  of rules. All decisions are based on the number of occupied
#   seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or 
#   diagonal from the seat). The following rules are applied to every seat simultaneously:

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# Floor (.) never changes; seats don't move, and nobody sits on the floor.

# After one round of these rules, every seat in the example layout becomes occupied:

second='''#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##'''
# After a second round, the seats with four or more occupied adjacent seats become empty again:

third='''#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##'''
# This process continues for three more rounds:

fourth='''#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##'''

fifth='''#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##'''

sixth='''#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##'''

# At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause 
# no seats to change state! Once people stop moving around, you count 37 occupied seats.

# Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

class SeatMatrix:
    def __init__(self, lines: str):
        self.state: List[str] = lines.splitlines()

    def isEmpty(self, row: int, col: int) -> bool:
        return self.state[row][col] == 'L'
    def isFloor(self, row: int, col: int) -> bool:
        return self.state[row][col] == '.'
    def isOccupied(self, row: int, col: int) -> bool:
        return self.state[row][col] == '#'

    def rows(self) -> int:
        return len(self.state)

    def cols(self) -> int:
        return len(self.state[0])

    def validate(self, row: int, col: int) -> bool:
        return (row >= 0 and row < len(self.state)) and (col >= 0 and col < len(self.state[0]))

    def takeSeat(self, row: int, col: int):
        if not self.isFloor(row, col):
            s = self.state[row]
            self.state[row] = mutateString(s, col, '#')
    
    def freeSeat(self, row: int, col: int):
        if not self.isFloor(row, col):
            s = self.state[row]
            self.state[row] = mutateString(s, col, 'L')

    def numberOfOccupiedNei(self, row: int, col: int) -> int:
        if not self.validate(row, col):
            raise Exception(f'invalid idx {row}; {col}')

        idx = self.adjecentIdxs(row, col)
        out = 0

        for i in idx:
            if self.isOccupied(i[0],i[1]):
                out += 1
        return out

    def numberOfOccupiedSeats(self) -> int:
        out = 0
        for r in self.rows():
            for c in self.cols():
                if self.isOccupied(r,c):
                    out += 1
        return out

    def adjecentIdxs(self, row: int, col: int) -> List[Tuple[int,int]]:
        return adjecentIdxs(row, col, self.rows(), self.cols())
        
    def __eq__(self, other) -> bool:
        if other is None or type(other) != SeatMatrix:
            return False
        if len(self.state) != len(other.state):
            return False

        for i in range(len(self.state)):
            if self.state[i] != other.state[i]:
                return False
        return True
    
    def __hash__(self) -> int:
        h = 0
        for i in self.state:
            h += hash(i)
        return h

def validateInput(data: str) -> bool:
    rows: List[str] = data.splitlines()
    numberOfCols = set(map(lambda x: len(x), rows))
    return len(numberOfCols) == 1

def mutateString(s: str, idx: int, newChar: str) -> str:
    assert len(newChar) == 1
    assert idx >=0 and idx < len(s)
    return s[0:idx] + newChar + s[idx+1:]

def adjecentIdxs(row: int, col: int, rowLen: int, colLen: int) -> List[Tuple[int,int]]:
    candidates = []
    for r in [-1,0,1]:
        for c in [-1,0,1]:
            rNei = row + r
            cNei = col + c
            if (r != 0 or c != 0) and (rNei >=0 and rNei < rowLen) and (cNei >= 0 and cNei < colLen):
                candidates.append((rNei, cNei))
    return candidates


assert mutateString('abcd', 0, 'x') == 'xbcd'
assert mutateString('abcd', 1, 'x') == 'axcd'
assert mutateString('abcd', 2, 'x') == 'abxd'
assert mutateString('abcd', 3, 'x') == 'abcx'

# 012
# 345
# 678
assert adjecentIdxs(0,0,3,3) == [(0,1),(1,0),(1,1)]
assert adjecentIdxs(0,1,3,3) == [(0,0),(0,2),(1,0),(1,1),(1,2)]
assert adjecentIdxs(2,2,3,3) == [(1,1),(1,2),(2,1)]
assert adjecentIdxs(1,1,3,3) == [(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)]


def simulate(seats: SeatMatrix) -> SeatMatrix:
    toOccupy: List[Tuple[int,int]] = []
    toFree: List[Tuple[int,int]] = []

    for row in range(seats.rows()):
        for col in range(seats.cols()):
            if seats.isFloor(row, col):
                continue

            numOfNei = seats.numberOfOccupiedNei(row, col)
            if seats.isEmpty(row,col) and numOfNei == 0:
                toOccupy.append((row, col))
            elif seats.isOccupied(row, col) and numOfNei >= 4:
                toFree.append((row, col))
    
    for r,c in toOccupy:
        seats.takeSeat(r,c)
    for r,c in toFree:
        seats.freeSeat(r,c)

    return seats

def simulateAndCount(content: str) -> int:
    seats = SeatMatrix(content)
    h = hash(seats)
    steps = 0
    MAX_STEPS = 500
    while steps < MAX_STEPS:
        # print(f'running step {steps}')
        seats = simulate(seats)
        newHash = hash(seats)
        if h == newHash:
            return seats.numberOfOccupiedSeats()
        steps += 1

    raise Exception(f'invalid state!')


inputData = [first, second, third, fourth, fifth, sixth]
for i in inputData:
    assert validateInput(i)

seats = SeatMatrix(first)
assert seats == SeatMatrix(first)
assert simulate(seats) == SeatMatrix(second)
assert simulate(seats) == SeatMatrix(third)
assert simulate(seats) == SeatMatrix(fourth)
assert simulate(seats) == SeatMatrix(fifth)
assert simulate(seats) == SeatMatrix(sixth)
assert simulate(seats) == SeatMatrix(sixth)
assert simulate(seats) == SeatMatrix(sixth)

assert hash(SeatMatrix(first)) == hash(SeatMatrix(first))
assert hash(SeatMatrix(second)) == hash(SeatMatrix(second))
assert hash(SeatMatrix(third)) == hash(SeatMatrix(third))

assert SeatMatrix(first) == SeatMatrix(first)
assert SeatMatrix(second) == SeatMatrix(second)
assert SeatMatrix(third) == SeatMatrix(third)

assert hash(SeatMatrix(first)) != hash(SeatMatrix(fourth))
assert hash(SeatMatrix(first)) != hash(SeatMatrix(second))
assert hash(SeatMatrix(first)) != hash(SeatMatrix(third))

assert SeatMatrix(first) != SeatMatrix(fourth)
assert SeatMatrix(first) != SeatMatrix(second)
assert SeatMatrix(first) != SeatMatrix(third)

assert simulateAndCount(first) == 37