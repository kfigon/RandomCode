from typing import List

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
    def __init__(self, lines: List[str]):
        self.state: List[str] = lines

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

def validateInput(data: str) -> bool:
    rows: List[str] = data.splitlines()
    numberOfCols = set(map(lambda x: len(x), rows))
    return len(numberOfCols) == 1

def mutateString(s: str, idx: int, newChar: str) -> str:
    assert len(newChar) == 1
    assert idx >=0 and idx < len(s)

    return s[0:idx] + newChar + s[idx+1:]

inputData = [first, second, third, fourth, fifth, sixth]
for i in inputData:
    assert validateInput(i)

def simulate(seats: SeatMatrix) -> SeatMatrix:
    pass

# # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# Floor (.) never changes; seats don't move, and nobody sits on the floor.

