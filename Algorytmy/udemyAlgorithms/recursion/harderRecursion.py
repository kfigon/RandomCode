from typing import List, Callable, Any

# reverse a string
def reverseStr(a: str) -> str:
    if len(a) == 1:
        return a
    return a[-1] + reverseStr(a[:-1])

assert reverseStr('awesome') == 'emosewa'
assert reverseStr('abcde') == 'edcba'


def isPalindromeIter(a: str) -> bool:
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            return False
    return True

assert not isPalindromeIter('awesome')
assert not isPalindromeIter('foobar')
assert isPalindromeIter('tacocat')
assert isPalindromeIter('abba')
assert isPalindromeIter('abcba')
assert isPalindromeIter('amanaplanacanalpanama')
assert not isPalindromeIter('amanaplanacanalpandemonium')

# string read the same forward and backward
def isPalindrome(a: str) -> bool:
    if len(a) < 2:
        return True
    return (a[0] == a[-1]) and isPalindrome(a[1:-1])

assert not isPalindrome('awesome')
assert not isPalindrome('foobar')
assert isPalindrome('tacocat')
assert isPalindrome('abba')
assert isPalindrome('abcba')
assert isPalindrome('amanaplanacanalpanama')
assert not isPalindrome('amanaplanacanalpandemonium')

# array and callback. Return true if a single valye in array returns true
def someRecursive(tab: List[int], fun: Callable[[int],bool]) -> bool:
    if len(tab) == 1:
        return fun(tab[0])
    return fun(tab[0]) or someRecursive(tab[1:], fun)
    

isOdd: Callable[[int],bool] = lambda x: x % 2 != 0
assert someRecursive([1,2,3,4], isOdd)
assert someRecursive([4,6,8,9], isOdd)
assert not someRecursive([4,6,8], isOdd)
assert not someRecursive([4,6,8], lambda x: x > 10)

def isArray(x: Any) -> bool:
    return isinstance(x, List)

def flatten(tab: List[Any]) -> List[int]:
    out: List[int] = []
    if len(tab) == 0:
        return []

    if isArray(tab[0]):
        return out + flatten(tab[0]) + flatten(tab[1:])
    return out + [tab[0]] + flatten(tab[1:])

assert flatten([]) == []
assert flatten([1]) == [1]
assert flatten([1,2]) == [1,2]
assert flatten([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert flatten([1, 2, 3, [4, 5]]) == [1, 2, 3, 4, 5]
assert flatten([1, [2, [3, 4], [[5]]]]) == [1, 2, 3, 4, 5]
assert flatten([[1],[2],[3]]) == [1,2,3]
assert flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) == [1,2,3]