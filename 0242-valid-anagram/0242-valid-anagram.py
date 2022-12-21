class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False 
        
        freq = [0] * 26 
        for x in s:
            freq[ord(x)-ord('a')] += 1 
        
        for x in t:
            freq[ord(x)-ord('a')] -= 1 
        
        if len(set(freq)) != 1:
            return False
        else:
            return True
            
            
