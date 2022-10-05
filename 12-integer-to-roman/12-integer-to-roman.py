class Solution(object):
    def intToRoman(self, num):
        romanValues = [("I",1),("IV",4),("V",5),("IX",9),("X",10),("XL",40),("L",50),("XC",90),("C",100),("CD",400),("D",500),("CM",900),("M",1000)]
        
        lst = []
        
        for x in range(len(romanValues)-1,-1,-1):
            roman, integer = romanValues[x]
            if num // integer:
                numSymbols = num // integer
                lst.append(roman*numSymbols)
                num = num % integer
            if not num:
                break
        
        res = ''.join(lst)
        return res