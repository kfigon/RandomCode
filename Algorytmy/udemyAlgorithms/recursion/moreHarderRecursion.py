from typing import List, Dict, Any

# given array of strings, capitalize first letter of each 
# string in the array

def capitalizeString(x: str) -> str:
    # if len(x) == 1:
        # return x.upper()
    # return capitalizeString(x[0]) + x[1:]
    return x[0].upper() + x[1:]

def capitalizeFirst(tab: List[str]) -> List[str]:
    if len(tab) == 0:
        return []
    elif len(tab) == 1:
        # return [tab[0].capitalize()]
        return [capitalizeString(tab[0])]

    return capitalizeFirst([tab[0]]) + capitalizeFirst(tab[1:])

assert capitalizeFirst([]) == []
assert capitalizeFirst(['asd']) == ['Asd']
assert capitalizeFirst(['Asd']) == ['Asd']
assert capitalizeFirst(['car','taco','banana']) == ['Car','Taco','Banana']

# return sum of all even number in given dictionary. May contain nested dicts

def nestedEvenSum(x: Any) -> int:
    if isinstance(x, int):
        return x if x % 2 == 0 else 0
    elif not isinstance(x, Dict):
        return 0
    # how to do recursive? 
    # items = list(x.items())
    # del x[items[0][0]]
    # return nestedEvenSum(items[0][1]) + nestedEvenSum(x)
    out = 0
    for item in x.items():
        out += nestedEvenSum(item[1])
    return out

obj1 : Dict[str, Any] = {
  'outer': 2,
  'obj': {
    'inner': 2,
    'otherObj': {
      'superInner': 2,
      'notANumber': True,
      'alsoNotANumber': "yup"
    }
  },
  'foo': 3
}

obj2: Dict[str, Any] = {
  'a': 2,
  'b': {'b': 2, 'bb': {'b': 3, 'bb': {'b': 2}}},
  'c': {'c': {'c': 2}, 'cc': 'ball', 'ccc': 5},
  'd': 1,
  'e': {'e': {'e': 2}, 'ee': 'car'}
}

assert nestedEvenSum(obj1) ==  6
assert nestedEvenSum(obj2) == 10

# given array of words return new array containing each word capitalized
def capitalizedWords(tab: List[str]) -> List[str]:
    if len(tab) == 0:
        return []
    elif len(tab) == 1:
        return [tab[0].upper()]
    
    return capitalizedWords([tab[0]]) + capitalizedWords(tab[1:])

assert capitalizedWords(['i', 'am', 'learning', 'recursion']) == ['I', 'AM', 'LEARNING', 'RECURSION']

# takes a dict and finds all of the values which are
# numbers and convert to strings
def stringifyNumbers(ob: Any) -> Any:
    if not isinstance(ob, bool) and isinstance(ob, int): # isinstance(True/False, bool) -> True 
        return str(ob)
    elif isinstance(ob, Dict):
        for key in ob:
            newVal = stringifyNumbers(ob[key])
            ob[key] = newVal
    return ob

xax: Dict[str, Any] = {
    'num': 1,
    'test': [],
    'data': {
        'val': 4,
        'info': {
            'isRight': True,
            'random': 66
        }
    }
}
expectedStringified: Dict[str, Any] ={
    'num': '1',
    'test': [],
    'data': {
        'val': '4',
        'info': {
            'isRight': True,
            'random': '66'
        }
    }
}
assert stringifyNumbers(xax) == expectedStringified


# accept dictionary, return array of all strings values in object
def collectStrings(ob: Any) -> List[str]:
    out: List[str] = []
    if isinstance(ob, str):
        return [ob]
    elif isinstance(ob, Dict):
        for key in ob:
            out += collectStrings(ob[key])
    return out

objFoo: Dict[str, Any] = {
    'stuff': "foo",
    'data': {
        'val': {
            'thing': {
                'info': "bar",
                'moreInfo': {
                    'evenMoreInfo': {
                        'weMadeIt': "baz"
                    }
                }
            }
        }
    }
}

assert collectStrings(objFoo) == ['foo', 'bar', 'baz']
print('jest git ziomx')