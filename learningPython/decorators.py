import unittest

def incrementuj(x):
    return x+1

# przekazujemy do srodka funkcje i opakowujemy ja
def recznyDekorator(funkcja):
    def wrapper(arg):
        return funkcja(arg+100)
    return wrapper


def dekoFoo(funkcja):
    def wrapper(arg):
        return funkcja(arg+100)
    return wrapper

@dekoFoo
def incrementuj2(x):
    return x+1

class Test(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(10, incrementuj(9))
    
    def testReczny(self):
        foo = recznyDekorator(incrementuj)
        self.assertEqual(110, foo(9))

    def testDeco(self):
        self.assertEqual(110, incrementuj2(9))

if __name__ == '__main__':
    unittest.main()