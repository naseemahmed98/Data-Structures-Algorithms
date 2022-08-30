class Solution:
    def maximalNetworkRank(self, n, roads):
        hashMap = collections.defaultdict(set)
        res = 0 
        for x, y in roads:
            hashMap[x].add(y)
            hashMap[y].add(x)
        
        for x in range(n):
            for y in range(x+1,n):
                totalNetwork = len(hashMap[x]) + len(hashMap[y])
                if x in hashMap[y]:
                    res = max(res,totalNetwork-1)
                else:
                    res = max(res,totalNetwork)
        return res
                
        