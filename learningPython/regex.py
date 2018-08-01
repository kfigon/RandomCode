import unittest
import re

class Test(unittest.TestCase):
    
    def test1(self):
        text = "some text"
        pattern = "text"

        result = re.findall(pattern, text)[0]
        self.assertEqual("text", result)

    def test2(self):
        text = "some text"
        pattern = "some"

        regex = re.compile(pattern)
        match = regex.match(text)

        self.assertIsNotNone(match)
        self.assertEqual("some", match.group())

    def test3(self):
        text = 'text123'
        cases = [
            # pattern
            '.*123',
            'text.*']
        for p in cases:
            with self.subTest(name='searching {} in {}'.format(p, text)):
                self.assertRegex(text, p)


if __name__ == '__main__':
    unittest.main()