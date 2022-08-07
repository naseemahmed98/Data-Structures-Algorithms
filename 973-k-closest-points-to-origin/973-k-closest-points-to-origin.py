class Solution(object):
    def kClosest(self, points, k):
        minHeap = []
        for x, y in points:
            dist = ((x ** 2) + (y ** 2)) ** 0.5
            minHeap.append([dist, x, y])
       
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res
            
            
            
                      
        