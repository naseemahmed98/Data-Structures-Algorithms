class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        l, r = 0, len(y)-1
        while l < r:
            if y[l] != y[r]:
                return False
            l+= 1 
            r-=1
        return True
            
        