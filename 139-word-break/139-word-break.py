class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1 )
        dp[len(s)] = True
        for x in range(len(s)-1, -1, -1):
            for z in wordDict:
                if x + len(z) <= len(s):
                    if s[x:x+len(z)] == z:
                        dp[x] = dp[x+len(z)]
                if dp[x]:
                    break
        return dp[0]