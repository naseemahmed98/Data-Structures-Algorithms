class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heightsSorted = heights[:]
        heightsSorted.sort()
        res = 0 
        for x,y in zip(heights,heightsSorted):
            if x != y:
                res += 1 
        return res