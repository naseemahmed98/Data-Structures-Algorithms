class Solution(object):
    def isAnagram(self, s, t):
        if len(s) == len(t):
            for x in set(s):
                if s.count(x) != t.count(x):
                    return False
            return True
        return False
