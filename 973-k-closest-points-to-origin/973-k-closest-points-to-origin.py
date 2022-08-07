class Solution(object):
    def kClosest(self, points, k):
        x, y = 0, 0 
        res = []
        res2 = []
        for p in points:
            dis = ((p[0] ** 2) + (p[1] ** 2)) ** 0.5
            res.append([[p[0],p[1]],dis])
        
        res.sort(key = lambda x: x[1])
       
        for x in range(k):
            res[x] = res[x][0]
        return res[:k]
            
            
            
                      
        