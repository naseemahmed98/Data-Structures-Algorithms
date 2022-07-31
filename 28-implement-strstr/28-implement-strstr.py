class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0 
        
        for x in range(len(haystack) + 1 - len(needle)):
            if haystack[x:x+len(needle)] == needle:
                return x
        return -1