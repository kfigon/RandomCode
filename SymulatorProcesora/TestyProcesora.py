__author__ = 'kamil'

import unittest
from SymulatorProcesora.Procesor import *

class TestyRejestru(unittest.TestCase):
    def testInit(self):
        r = Rejestr(0x12)
        self.assertEqual(0x12, r.get())

    def testInit2(self):
        r = Rejestr()
        self.assertEqual(0, r.get())

    def testInitOverflow(self):
        r = Rejestr(0xffff1)
        self.assertEqual(0xfff1, r.get())

    def testGetUpper(self):
        r = Rejestr(0x12)
        self.assertEqual(0, r.getUpper())

    def testGetUpper2(self):
        r = Rejestr(0xf812)
        self.assertEqual(0xf8, r.getUpper())

    def testGetLower(self):
        r = Rejestr(0x12)
        self.assertEqual(0x12, r.getLower())

    def testGetLower2(self):
        r = Rejestr(0x5512)
        self.assertEqual(0x12, r.getLower())

    def testSetLower(self):
        r = Rejestr()
        r.setLower(3)
        self.assertEqual(0x3, r.get())

    def testSetLowerOverflow(self):
        r = Rejestr()
        r.setLower(0xff1)
        self.assertEqual(0xf1, r.get())

    def testSetUpper(self):
        r = Rejestr()
        r.setUpper(3)
        self.assertEqual(0x3, r.getUpper())
        self.assertEqual(0x300, r.get())

    def testSetUpperOverflow(self):
        r = Rejestr()
        r.setUpper(0x123)
        self.assertEqual(0x23, r.getUpper())

    def testToStr(self):
        r = Rejestr(0x5512)
        self.assertEqual("0x5512", str(r))

class TestyProcesora(unittest.TestCase):
    def setUp(self):
        self.p = Procesor()

    def testGetBasic(self):
        self.assertEqual(0, self.p.parseAndExecute('GET AL'))
        self.assertEqual(0, self.p.parseAndExecute('GET AH'))

        self.assertEqual(0, self.p.parseAndExecute('GET BL'))
        self.assertEqual(0, self.p.parseAndExecute('GET BH'))

        self.assertEqual(0, self.p.parseAndExecute('GET CL'))
        self.assertEqual(0, self.p.parseAndExecute('GET CH'))

        self.assertEqual(0, self.p.parseAndExecute('GET DL'))
        self.assertEqual(0, self.p.parseAndExecute('GET DH'))

    def testMov(self):
        self.p.parseAndExecute('MOV AL 0x12')
        self.assertEqual(0x12, self.p.parseAndExecute('GET AL'))

    def testAdd(self):
        self.p.parseAndExecute('MOV AL 0x12')
        self.p.parseAndExecute('MOV BH 0xDE')
        self.p.parseAndExecute('ADD AL BH')

        self.assertEqual(0xF0, self.p.parseAndExecute('GET AL'))
        self.assertEqual(0xDE, self.p.parseAndExecute('GET BH'))

    def testSub(self):
        self.p.parseAndExecute('MOV AL 0x12')
        self.p.parseAndExecute('MOV BH 0xDE')
        self.p.parseAndExecute('SUB BH AL')

        self.assertEqual(0x12, self.p.parseAndExecute('GET AL'))
        self.assertEqual(0xCC, self.p.parseAndExecute('GET BH'))

    def testToString(self):
        expected = "AX: 0x0\n" \
                   "BX: 0x0\n" \
                   "CX: 0x0\n" \
                   "DX: 0x0"
        self.assertEqual(expected, str(self.p))

if __name__ == '__main__':
    unittest.main()
