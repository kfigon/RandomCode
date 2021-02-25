from typing import List, Optional, Dict
import unittest

class Node:
    def __init__(self, val: str, freq: int):
        self.val: str = val
        self.freq: int = freq
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def isLeaf(self) -> bool:
        return self.left is None and self.right is None

class Tree:
    def __init__(self):
        self.root: Optional[Node] = None

    def build(self, inputStr: str):
        frequencies = calcFreq(inputStr)
        for key in frequencies:
            keysFrequency = frequencies[key]
        pass



    def huffman(self, inputStr: str) -> str:
        return ''

def calcFreq(inputStr: str) -> Dict[str,int]:
    frequencies: Dict[str, int] = {}
    for c in inputStr:
        if c in frequencies:
            frequencies[c] += 1
        else:
            frequencies[c] = 1
    # sort by value
    return dict(reversed(sorted(frequencies.items(), key=lambda item: item[1])))

def encode(inputStr: str, encodeChar: str) -> str:
    tree = Tree()
    tree.build(inputStr)
    return tree.huffman(encodeChar)

def decode(inputStr: str, sequenceToDecode: str) -> str:
    tree = Tree()
    tree.build(inputStr)
    return tree.decode(sequenceToDecode)

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual('0', encode('ABRACADABRA', 'A'))
        self.assertEqual('111', encode('ABRACADABRA', 'B'))
        self.assertEqual('1100', encode('ABRACADABRA', 'C'))
        self.assertEqual('1101', encode('ABRACADABRA', 'D'))
        self.assertEqual('10', encode('ABRACADABRA', 'R'))

    def test2(self):
        self.assertEqual('A', decode('ABRACADABRA', '0'))
        self.assertEqual('B', decode('ABRACADABRA', '111'))
        self.assertEqual('C', decode('ABRACADABRA', '1100'))
        self.assertEqual('D', decode('ABRACADABRA', '1101'))
        self.assertEqual('R', decode('ABRACADABRA', '10'))

    def decodeMoreComplicated(self):
        self.assertEqual('ABRACADABRA', decode('ABRACADABRA', '01111001100011010111100'))

if __name__ == '__main__':
    unittest.main()