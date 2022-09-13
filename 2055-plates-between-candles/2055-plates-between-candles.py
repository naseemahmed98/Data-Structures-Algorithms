class Solution(object):
    def platesBetweenCandles(self, s, queries):
        numStars = [0] * len(s)
        if s[0] == "*":
            numStars[0] = 1 
        
        leftArray = [-1] * len(s)
        if s[0] == "|":
            leftArray[0] = 0 
        
        for x in range(1,len(s)):
            if s[x] == "*":
                numStars[x] = 1 + numStars[x-1]
                leftArray[x] = leftArray[x-1]
            else:
                numStars[x] = numStars[x-1]
                leftArray[x] = x 
        
        rightArray = [float("inf")] * len(s)
        if s[-1] == "|":
            rightArray[-1] = len(s)-1
        for x in range(len(s)-2,-1,-1):
            if s[x] == "|":
                rightArray[x] = x 
            else:
                rightArray[x] = rightArray[x+1]
        
        res = []
        for x,y in queries:
            leftIndex, rightIndex = rightArray[x], leftArray[y]
            if rightIndex - leftIndex > 1:
                res.append(numStars[rightIndex]-numStars[leftIndex])
            else:
                res.append(0)
        return res            
            