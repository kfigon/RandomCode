import unittest

def matchingParents(parents: str) -> bool:
    stak = []
    closing = {
        '{': '}',
        '(': ')',
        '[': ']',
    }
    for c in parents:
        if c in closing:
            stak.append(c)
        elif len(c) == 0 or closing[stak.pop()] != c:
            return False
    return len(stak) == 0

class TestStack(unittest.TestCase):
    def testMatchingParenthesis(self):
        data = [
            ('[][]()(){}', True),
            ('[([])]', True),
            ('[()[()]([])]', True),
            ('{[(())}', False),
            ('{', False),
            ('[[))', False),
            ('[[}', False),
            ('{[((])}', False),
            ('{[((])', False),
            ('{[(()])}', False),
        ]
        for d in data:
            with self.subTest(d[0]):
                self.assertEqual(d[1], matchingParents(d[0]))

if __name__ == "__main__":
    unittest.main()