class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp = [ [0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        for x in range(len(text1)-1,-1,-1):
            for y in range(len(text2)-1,-1,-1):
                if text1[x] == text2[y]:
                    dp[x][y] = 1 + dp[x+1][y+1]
                else:
                    dp[x][y] = max(dp[x+1][y],dp[x][y+1])
        
        return dp[0][0]