class Solution(object):
    def longestPalindrome(self, s):
        def construct_string(l, r, max_string):
            while l >= 0 and r < len(s) and s[l].upper() == s[r].upper():
                if (r - l + 1) > len(max_string):
                    max_string = s[l:r+1]
                l -= 1
                r += 1
            return max_string
        
        max_string = ""
        for x in range(len(s)):
            l, r = x, x
            max_string = construct_string(l, r, max_string)
            l, r = x, x + 1
            max_string = construct_string(l, r, max_string)
        return max_string
           







         

