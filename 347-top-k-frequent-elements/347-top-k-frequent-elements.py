class Solution(object):
    def topKFrequent(self, nums, k):
     
        res = []
        freq = dict()
        
        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        
        
        for num, fr in freq.items():
            
            if len(res) < k:
                heapq.heappush(res,(fr,num))
            else:
                heapq.heappushpop(res, (fr,num))
            #print(res)
        
        return [num for fr,num in res]
        