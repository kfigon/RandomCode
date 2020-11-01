from typing import List

# optimization problems
# looking for global maximum

# overlaping subproblems - mozemy rozbic problem na mniejsze i te
#  mniejsze mozna reuzyc (np. fibonnaci - poszczegolne podwyniki mozna wykorzystac, a nie obliczac ponownie)

# optimal substructure - optymalny wynik moze byc skonstruowany z
# optymalnych wynikow podproblemow

# fib(5) - fib(3) jest liczone 2 razy, performance bardzo slaby O(2^n)
def fib(n: int) -> int:
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# O(n)
def fibDynamic(n: int) -> int:
    lookup: List[int] = [0,1,1]
    def foo(n: int) -> int:
        if len(lookup) > n:
            return lookup[n-1] + lookup[n-2]
        res = foo(n-1) + foo(n-2)
        lookup.append(res)
        return res

    return foo(n)

def fibDynamic2(n: int) -> int:
    if n<=2:
        return 1
    fibs = [0,1,1]
    for i in range(3, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n]

assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
assert fib(7) == 13
assert fib(8) == 21
assert fib(29) == 514229
assert fib(35) == 9227465
# assert fib(55) == 139583862445
print('recursive done')
assert fibDynamic(2) == 1
assert fibDynamic(4) == 3
assert fibDynamic(5) == 5
assert fibDynamic(6) == 8
assert fibDynamic(7) == 13
assert fibDynamic(8) == 21
assert fibDynamic(29) == 514229
assert fibDynamic(35) == 9227465
assert fibDynamic(55) == 139583862445

assert fibDynamic2(2) == 1
assert fibDynamic2(4) == 3
assert fibDynamic2(5) == 5
assert fibDynamic2(6) == 8
assert fibDynamic2(7) == 13
assert fibDynamic2(8) == 21
assert fibDynamic2(29) == 514229
assert fibDynamic2(35) == 9227465
assert fibDynamic2(55) == 139583862445
print('ok')