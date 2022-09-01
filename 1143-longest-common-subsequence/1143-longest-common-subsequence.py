class Solution:
    def longestCommonSubsequence(self, text1,text2):
        def recurMe(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j]=1+recurMe(i+1,j+1)
                return dp[i][j]
            else:
                dp[i][j]=max(recurMe(i+1,j),recurMe(i,j+1))
                return dp[i][j]
        dp=[[-1 for j in range(len(text2))] for i in range(len(text1))]
        
        a = recurMe(0,0)
        print(dp)
        return a