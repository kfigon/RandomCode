import unittest

# Number letter counts
# Problem 17 
# If the numbers 1 to 5 are written out in words: one, two, three,
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example,
# 342 (three hundred and forty-two) contains 23
# letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and"
# when writing out numbers is in compliance with British usage.

def getNum(num):
    #<0;19>
    jednosci = ["", 'one','two','three','four','five','six','seven',
                'eight','nine','ten', 'eleven','twelve','thirteen',
                'fourteen','fifteen','sixteen','seventeen','eighteen',
                'nineteen']
    # <20;90>
    dziesiatki = ['','twenty','thirty','forty','fifty','sixty','seventy',
                  'eighty','ninety']
    setki = "hundred"
    tysiac = 'onethousand'
    
    out=""
    if(num >=0 and num <= 19):
        return jednosci[num]
    elif(num < 100):        
        out += dziesiatki[int(num/10)-1] + jednosci[num%10]
    elif(num < 1000):
        ileSetek = int(num/100)
        out += jednosci[ileSetek] + setki
        if(num%100 != 0):
            ileDziesiatek = num//10 - ileSetek*10
            if(ileDziesiatek ==0):
                ileDziesiatek+=1
            out+='and'+dziesiatki[ileDziesiatek-1] +jednosci[num%10]
    else:
        out+=tysiac
        
    return out
    
def foo(tab):
    totalLen = 0
    for num in tab:
        totalLen += len(getNum(num))

    return totalLen
    
class Testy(unittest.TestCase):
    def test1(self):
        self.assertEqual(19, foo([1,2,3,4,5]))
    def testUltimate(self):
        tab =[0]*1000
        for i in range(len(tab)):
            tab[i] = i+1

        self.assertEqual(21124, foo(tab))
        
    def testyGetNum(self):
        self.assertEqual('one', getNum(1))
        self.assertEqual('two', getNum(2))
        self.assertEqual('five', getNum(5))

    def testyGenNumDziesiatki(self):
        self.assertEqual('twentytwo', getNum(22))
        self.assertEqual('seventysix', getNum(76))
        self.assertEqual('sixtyeight', getNum(68))
        self.assertEqual('seventy', getNum(70))
        self.assertEqual('sixtyfive', getNum(65))
        
    def testyGenNumSetki(self):
        self.assertEqual('onehundred', getNum(100))
        self.assertEqual('twohundred', getNum(200))
        self.assertEqual('onehundredandtwentytwo', getNum(122))
        self.assertEqual('fivehundredandseventysix', getNum(576))
        self.assertEqual('sevenhundredandsixtyeight', getNum(768))
        self.assertEqual('fivehundredandninetyfive', getNum(595))
        self.assertEqual('ninehundredandninetynine', getNum(999))
        self.assertEqual('onehundredandfive', getNum(105))
        

if __name__=="__main__":
    unittest.main()
