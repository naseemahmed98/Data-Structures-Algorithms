class Solution(object):
    def wordBreak(self, s, wordDict):
        s_len = len(s)
        
        # initialize the DP talbe. 
        dp = [False] * (s_len + 1)
        # start from empty string as the seed. 
        dp[0] = True
        
        # building the DP table.
        for i in range(s_len):
            if dp[i]:
                for w in wordDict:
                    print(i)
                    if i + len(w) <= s_len and s[i:i + len(w)] == w:
                        dp[i + len(w)] = True
        
        # our result is the dp[s_len]
        return dp[s_len]