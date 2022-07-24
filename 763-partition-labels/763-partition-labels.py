class Solution(object):
    def partitionLabels(self, s):
        last_index = {}
        res = []
        for x, y in enumerate(s):
            last_index[y] = x 
        
        size, end = 0, 0 
        for x, y in enumerate(s):
            size += 1 
            end = max(end,last_index[y])
            if x == end:
                res.append(size)
                size = 0 
        return res
            
            
            
        