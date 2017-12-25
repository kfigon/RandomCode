import unittest

def splot(x,y):
    out =[0]*(len(x)+len(y)-1)
    
    for idxSplotu in range(len(out)):
        for idxWew in range(len(out)):
            xEl=0 #x - ten odwracam!
            yEl=0 #y 
            idxX = idxSplotu-idxWew
            idxY = idxWew
            if(idxX >=0 and idxX < len(x)):
                xEl = x[idxX]
            if(idxY >=0 and idxY < len(y)):
                yEl = y[idxY]
            out[idxSplotu] += xEl * yEl
        
    return out

class TestySplotu(unittest.TestCase):
    def test1(self):
        self.assertEqual([2,7,18,41,50,52,40], splot([1,2,4,8],[2,3,4,5]))

    def test2(self):
        self.assertEqual([9,9,11,5,2], splot([3,1,2],[3,2,1]))

if __name__ == "__main__":
    unittest.main()
