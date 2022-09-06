class Solution:
    def combinationSum(self, candidates : List[int], target: int) -> List[List[int]]:    
        dp = [[] for x in range(target+1)]
        
        for x in candidates:
            if x <= target:
                dp[x].append([x])
            for y in range(x+1,target+1):
                for z in dp[y-x]:
                    dp[y].append(z + [x])
        return dp[-1]
                
        
        