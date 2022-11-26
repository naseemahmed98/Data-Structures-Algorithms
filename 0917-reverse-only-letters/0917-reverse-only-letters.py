class Solution(object):
    def reverseOnlyLetters(self, s):
        res = []
        j = len(s) -1 
        for x in s:
            if x.isalpha():
                while not s[j].isalpha():
                    j -=1 
                res.append(s[j])
                j-=1 
            else:
                res.append(x)
        return "".join(res)