import unittest

# wymaga zewnetrznego toola mypy zeby sprawdzil kod

def greeting(napis: str) -> str:
    return "hello " + napis

def oldschoolGreet(napis):
    return "hello " + str(napis)

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual("hello asd", greeting("asd"))

    def test2(self):
        self.assertRaises(TypeError, greeting, 123)

    def test3(self):
        self.assertEqual("hello 123", oldschoolGreet(123))

if __name__ == '__main__':
    unittest.main()