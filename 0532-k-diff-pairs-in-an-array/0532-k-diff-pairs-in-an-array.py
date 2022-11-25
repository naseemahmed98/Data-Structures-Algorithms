class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pairs = set()
        res = 0 
        differences = {}
        for x in nums:  
            if -1 * (k-x) in differences and (x,-1 * (k-x)) not in pairs:
                res +=1 
                pairs.add((x,-1*(k-x)))
                pairs.add((-1*(k-x),x))
            
            if (k + x) in differences and (x,k+x) not in pairs:
                res += 1 
                pairs.add((x,k+x))
                pairs.add((k+x,x))
            
            differences[x] = 1
        return res 
        