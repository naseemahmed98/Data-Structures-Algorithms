class Solution:
    def combinationSum(self, candidates : List[int], target: int) -> List[List[int]]:    
        dp = [[] for i in range(target+1)]
        for x in candidates :
            if x <= target:
                dp[x].append([x]) 
            for y in range(x, target+1):# x+1 to target(include)
                for lst in dp[y-x]:
                    dp[y].append(lst+[x])
    
        return dp[-1]
                
        
        