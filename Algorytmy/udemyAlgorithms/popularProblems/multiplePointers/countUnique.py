from typing import List

# input - sorted array
# count unique values in the array

# O(n)
def countUnique(tab: List[int]) -> int:
    if len(tab) == 0:
        return 0
    # print(f"\n\nsearching {len(tab)}")
    # numberOfIterations = 0
    numberPointer = 0
    diffPointer = 1
    uniqueCounter = 1
    while numberPointer < len(tab) and diffPointer < len(tab):
        # numberOfIterations +=1
        if tab[diffPointer] == tab[numberPointer]:
            diffPointer += 1
        else:
            numberPointer = diffPointer
            diffPointer += 1
            uniqueCounter += 1
    # print(f"number of interations {numberOfIterations}")
    return uniqueCounter


# O(n^2)
def countUniqueBrute(tab: List[int]) -> int:
    unique: List[int] = []
    for i in tab:
        if i not in unique:
            unique.append(i)
    return len(unique)

assert countUnique([1,1,1,1,1,2]) == 2
assert countUnique([1,2,3,4,4,4,7,7,7,12,12,13]) == 7
assert countUnique([]) == 0
assert countUnique([-2,-1,-1,0,1]) == 4
assert countUnique([4]) == 1
assert countUnique([1,2,2,5,7,7,99]) == 5

assert countUniqueBrute([1,1,1,1,1,2]) == 2
assert countUniqueBrute([1,2,3,4,4,4,7,7,7,12,12,13]) == 7
assert countUniqueBrute([]) == 0
assert countUniqueBrute([-2,-1,-1,0,1]) == 4
assert countUniqueBrute([4]) == 1
assert countUniqueBrute([1,2,2,5,7,7,99]) == 5
print('ok')