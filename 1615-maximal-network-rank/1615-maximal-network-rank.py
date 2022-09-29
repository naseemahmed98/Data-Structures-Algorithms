class Solution:
    def maximalNetworkRank(self, n,roads):
        hashmap=collections.defaultdict(set)
        for x,y in roads:
            hashmap[x].add(y)
            hashmap[y].add(x)
        
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                totalNetwork = len(hashmap[i]) + len(hashmap[j])
                if j in hashmap[i]:
                    res=max(res,totalNetwork-1)
                else:
                    res=max(res,totalNetwork)
        return res