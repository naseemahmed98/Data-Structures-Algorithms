class Solution(object):
    def twoSumLessThanK(self, movieTimes, duration):
        indices = {}
        for x in range(len(movieTimes)):
            if movieTimes[x] not in indices:
                indices[movieTimes[x]] = x
        movieSum = duration 
        movieTimes.sort() #60,75,85,90,120,125,150
        l, r = 0,len(movieTimes)-1 
        largestPossibleSum = float("-inf")
        while l < r: 
            if movieTimes[r] + movieTimes[l] >= movieSum:
                r -= 1 
            if movieTimes[r] + movieTimes[l] < movieSum:
                if movieTimes[r] + movieTimes[l] > largestPossibleSum:
                    largestPossibleSum = movieTimes[l] + movieTimes[r]

                l += 1 
        return largestPossibleSum if largestPossibleSum > float("-inf") else -1 
        