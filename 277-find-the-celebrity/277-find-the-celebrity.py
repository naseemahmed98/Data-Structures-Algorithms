# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution:
    def findCelebrity(self, n):
        celebrity = 0 
        for x in range(1,n):
            if knows(celebrity,x) == 1:
                celebrity = x 
        
        for x in range(n):
            if x == celebrity:
                continue
            if knows(celebrity,x) == 1 or knows(x,celebrity) == 0:
                return -1 
        
        return celebrity

            
        