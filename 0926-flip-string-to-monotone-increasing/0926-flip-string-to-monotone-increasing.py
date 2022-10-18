class Solution(object):
    def minFlipsMonoIncr(self, s):
        flips, zeros =  0, 0
        for x in range(len(s)-1,-1,-1):
            if s[x] == "0":
                zeros += 1 
            else:
                flips = min(flips+1,zeros)
        return flips









