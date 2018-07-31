import unittest

class A:
    def __init__(self, arg):
        self.arg = arg
    
    def foo(self):
        return self.arg

class B(A):
    def __init__(self):
        super().__init__(3)

    def foo(self):
        return 123


class Test(unittest.TestCase):
    def test(self):
        a = A(3)
        self.assertEqual(3, a.foo())

        b = B()
        self.assertEqual(123, b.foo())
        self.assertEqual(3, b.arg)

if __name__ == '__main__':
    unittest.main()