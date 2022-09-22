class Solution(object):
    def minFlipsMonoIncr(self, s):
        numOnes = flips = 0
        for c in s:
            if c == '1':
                numOnes += 1
            else:
                flips = min(flips+1, numOnes)     
        return flips










