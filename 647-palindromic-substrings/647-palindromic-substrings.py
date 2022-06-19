class Solution(object):
    def countSubstrings(self, s):
        def verify_palindromic(l, r, counter):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counter += 1 
                l -= 1 
                r += 1 
            return counter 
        
        counter = 0 
        for x in range(len(s)):
            l, r = x, x
            counter = verify_palindromic(l,r,counter)
            l, r = x, x+1 
            counter = verify_palindromic(l,r,counter)
        return counter
            
        