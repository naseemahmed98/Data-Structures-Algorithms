class Solution:
    def maximalNetworkRank(self, n,roads):
        hashmap={}
        
        for i in range(n):
            hashmap[i]=[]
        for x,y in roads:
            hashmap[x].append(y)
            hashmap[y].append(x)
        print(hashmap)
        final=[]
        maxlen=0
        for i in range(n):
            for j in range(i+1,n):
                if j in hashmap[i]:
                    a=hashmap[i]
                    b=hashmap[j]
                    final=a+b
                    maxlen=max(maxlen,len(final)-1)
                else:
                    a=hashmap[i]
                    b=hashmap[j]
                    final=a+b
                    maxlen=max(maxlen,len(final))
        return maxlen