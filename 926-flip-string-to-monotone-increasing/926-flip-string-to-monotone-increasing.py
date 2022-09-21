class Solution(object):
    def minFlipsMonoIncr(self, s):
        Ts = flips = 0
        for c in s:
            if c == '1':
                Ts += 1
            else:
                flips = min(flips+1, Ts)     
        return flips










