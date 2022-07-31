class Solution(object):
    def firstUniqChar(self, s):
        frequency = {}
        for x in range(len(s)):
            if s[x] not in frequency:
                frequency[s[x]] = 1
            else:
                frequency[s[x]] += 1 
        for x in range(len(s)):
            if frequency[s[x]] == 1:
                return x
        return -1
        