class Solution(object):
    def lengthOfLongestSubstring(self,s):
        if len(s) == 0 or len(s) == 1:
            return len(s)
        res = 1
        unique = set()
        l, r = 0, 0
        while r < len(s):
            while s[r] in unique:
                unique.remove(s[l])
                l+=1
            
            unique.add(s[r])
            res = max(r - l +1, res)
            
            r += 1 
       
        return res 

            
            
        
        