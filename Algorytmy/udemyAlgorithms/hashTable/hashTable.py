from typing import Optional, List, Tuple

# hash table == hash map == dictionary

# - to store key-value pairs
# - elements are not ordered
# - turbo fast for find/remove/add - very commonly used

# inside regular array, but we change string to number and store
# change string to number - hash
# map 'pink' -> 0
class HashTable:
    def __init__(self, arrayLen = 19):
        self.tab: List[List[Tuple[str, str]]] = [[] for _ in range(arrayLen)] # it's good to have the length as prime number to reduce collisions

# collision handling approaches
# separate chaining - store elements in the same position by using linked list or array
# linear probing - find next empty slot when collision

# here separate chaining:
    def put(self, key: str, val: str):
        hashVal = myBetterHashFun(key, len(self.tab))
        toAdd = (key, val)
        for el in self.tab[hashVal]:
            if el[0] == key:
                raise Exception(f'Duplicated key {key}')
            
        self.tab[hashVal].append(toAdd)
            
    def get(self, key: str) -> str:
        hashVal = myBetterHashFun(key, len(self.tab))
        candidate = self.tab[hashVal]
        for i in candidate:
            if i[0] == key:
                return i[1]
        raise Exception(f'Key error - {key} does not exist')

    def keys(self) -> List[str]:
        out: List[str] = []
        for el in self.tab:
            for i in el:
                out.append(i[0])
        return out
    
    def values(self) -> List[str]:
        out: List[str] = []
        for el in self.tab:
            for i in el:
                if i[1] not in out:
                    out.append(i[1])
        return out

# hash can't be worked backwards
# hashes can repeat, there can be collisions
# deterministic - hashes generate the same value for the same data consistently
# fast (e.g. constant time)
# uniform distribution (evenly distributed)

# key and length of array, so hash is between <0;len)
def myHashFun(key: str, length: int) -> int:
    return sum(map(lambda c: ord(c)-ord('a')+1, key)) % length
    # this has flaws, it's not constant time, could be more random, hashes only strings

# using min() we limit loop
# prime number makes distribution more random and spread, reduces collisions
def myBetterHashFun(key: str, length: int) -> int:
    v = 0
    foo = min(len(key), 100)
    weirdPrimeNumber = 31
    for c in range(foo):
        codeVal = ord(key[c])-96
        v = (v*weirdPrimeNumber+codeVal) % length
    # print(f'{key} -> {v}')
    return v