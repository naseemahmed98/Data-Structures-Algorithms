class Solution:
    def longestCommonSubsequence(self, text1,text2):
        def topDown(x,y):
            if x == len(text1) or y == len(text2):
                return 0 
            if dp[x][y] != 0:
                return dp[x][y]
            if text1[x] == text2[y]:
                dp[x][y] = 1 + topDown(x+1,y+1)
                return dp[x][y]
            else:
                dp[x][y] = max(topDown(x+1,y),topDown(x,y+1))
                return dp[x][y]
        
        dp = [[0 for y in range(len(text2))] for x in range(len(text1))]
        return topDown(0,0)
        