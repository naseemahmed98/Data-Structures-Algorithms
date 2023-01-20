class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0 
        uniqueLetters = set()
        l, r = 0, 0
        res = 1
        while r < len(s):
            while s[r] in uniqueLetters:
                uniqueLetters.remove(s[l])
                l+=1 
            
            uniqueLetters.add(s[r])
            res = max(res,r-l+1)
                
            r+=1 
        return res