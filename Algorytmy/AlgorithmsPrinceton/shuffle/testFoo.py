from typing import List
from operator import itemgetter
import random

#  wygenerowac dla kazdego entry random i posortowac wg tego
def shuffleSort(tab: List[int]) -> List[int]:
    helperTable: List[int] = [random.randint(0,100) for _ in range(len(tab))]
    foo = [(tab[i], helperTable[i]) for i in range(len(tab))]
    foo.sort(key=itemgetter(1))
    return list(map(lambda el: el[0], foo))

# szybsze!
def knuthShufftle(tab: List[int]) -> List[int]:
    out = [i for i in tab]
    for i in range(len(tab)):
        r = random.randint(0, i)
        out[i],out[r] = out[r],out[i]
    return out

if __name__ == "__main__":
    for i in range(5):
        tab = [i for i in range(random.randint(8,11))]
        tab.sort()
        print(tab)
        print(shuffleSort(tab))
        print(knuthShufftle(tab))
        print()