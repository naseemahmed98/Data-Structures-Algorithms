class Solution(object):
    def lengthOfLongestSubstring(self,s):
        seen = set()
        res = j = 0
        
        for i in s:
            while i in seen:
                seen.remove(s[j])
                j += 1
            seen.add(i)
            
            res = max(res, len(seen))
        
        return res

            
            
        
        