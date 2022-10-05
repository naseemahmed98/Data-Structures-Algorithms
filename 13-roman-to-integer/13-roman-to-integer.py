class Solution(object):
    def romanToInt(self, s):
        romanValues = {"I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        res = 0 
        for x in range(len(s)):
            if x < len(s)-1 and romanValues[s[x]] < romanValues[s[x+1]]:
                res -= romanValues[s[x]]
            else:
                res += romanValues[s[x]]
        
        return res
                
                