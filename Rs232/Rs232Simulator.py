import unittest

class Rs232:
    FRAME_LEN = 1 + 8 + 1 +1
    def __init__(self):
        pass

    # start - 0
    # 8 bitow LE
    # parity
    # stop 1
    def encode(self, data):
        out = [0] *(len(data) * self.FRAME_LEN)
        for dataIdx in range(len(data)):
            el = data[dataIdx]
            encodedChar = self.__encodeSingleLetter(el)
            i=0
            while(i < self.FRAME_LEN):
                out[dataIdx*self.FRAME_LEN + i] = encodedChar[i]
                i+=1
        return out
    def __encodeSingleLetter(self, data):
        liczba = ord(data)
        binary = '{:08b}'.format(liczba) 
        # reverse it

        liczbaJedynek = 0
        out = [0]* self.FRAME_LEN
        for i in range(1,len(out)):
            if(i < 9):
                bit = int(binary[len(binary) - i])
                out[i] = bit
                if(bit == 1):
                    liczbaJedynek+=1
            elif(i == 9):
                if(liczbaJedynek % 2 ==1):
                    out[i] = 1
            else:
                out[i] = 1 # stop
        
        return out
    
    def decode(self, data):
        out=""
        for newCharIdx in range(0, len(data), self.FRAME_LEN):
            
            singleChar = data[newCharIdx:newCharIdx+self.FRAME_LEN]
            out += self.__decodeChar(singleChar)
            
        return out
    def __decodeChar(self, data):
        out=[0]*self.FRAME_LEN
        binary = reversed(data[1:9])
        string = ""
        for i in binary:
            string += str(i)
        return chr(int(string, 2))
        
class TestRs232(unittest.TestCase):
    def testEncode(self):
        r = Rs232()
        # 01100001
        self.assertEqual([0,  1,0,0,0,0,1,1,0,  1,1], r.encode('a'))  
        self.assertEqual([0,  0,1,0,0,0,1,1,0,  1,1], r.encode('b'))
        # 01111010
        self.assertEqual([0,  0,1,0,1,1,1,1,0,  1,1], r.encode('z'))
        #01000001
        self.assertEqual([0,  1,0,0,0,0,0,1,0,  0,1], r.encode('A'))
        #01011010
        self.assertEqual([0,  0,1,0,1,1,0,1,0,  0,1], r.encode('Z'))

    def testEncodeStream(self):
        exp = [0,  1,0,0,0,0,1,1,0,  1,1,
               0,  0,1,0,0,0,1,1,0,  1,1,
               0,  0,1,0,1,1,1,1,0,  1,1]
        r= Rs232()
        self.assertEqual(exp, r.encode('abz'))

    def testDecode(self):
        r = Rs232()
        self.assertEqual('z', r.decode([0,  0,1,0,1,1,1,1,0,  1,1]))

    def testDecodeStream(self):
        data = [0,  1,0,0,0,0,1,1,0,  1,1,
               0,  0,1,0,0,0,1,1,0,  1,1,
               0,  0,1,0,1,1,1,1,0,  1,1]
        r = Rs232()
        self.assertEqual('abz', r.decode(data))
        
if __name__ == "__main__":
    unittest.main()
