class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        dp = [[] for x in range(n+1)]
        for x in range(n):
            if x >= 10:
                break
            dp[x].append([x])
            for y in range(x+1,n+1):
                for z in dp[y-x]:
                    dp[y].append(z + [x])
        for x in dp[-1]:
            if len(x) == k and len(set(x)) == len(x):
                res.append(x)
        return res
                        