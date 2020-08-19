from typing import List, Callable
import math

# https://pl.wikipedia.org/wiki/Sito_Eratostenesa
# https://pl.spoj.com/problems/latwe/
def isPrimeEratostenes(x: int) -> bool:
    if x < 2:
        raise Exception(f'invalid num {x}')
    if x == 2:
        return True

    sito :List[bool] = [False for i in range(x+1)]
    boundary = int(math.sqrt(x))

    for i in range()


    return sito[x]

def isPrimeNaive(x :int) -> bool:
    if x < 2:
        raise Exception(f'invalid num {x}')
    
    for i in range(2,x):
        if x % i == 0:
            return False

    return True

pierwsze :List[int] = [2, 3, 5, 7, 11, 13, 
17, 19, 23, 29, 31, 37, 
41, 43, 47, 53, 59, 61, 67, 
71, 73, 79, 83, 89, 97]

niePierwsze :List[int] = [4,6, 8,9,10,12,
14,15,16,18,20,21,22,24,25,26,27,28,30]

def doTests(foo: Callable[[int],bool]):
    for i in pierwsze:
        assert foo(i) == True, f'{i} should be prime'

    for i in niePierwsze:
        assert foo(i) == False, f'{i} should NOT be prime'

    print("done!")

doTests(isPrimeNaive)
doTests(isPrimeEratostenes)