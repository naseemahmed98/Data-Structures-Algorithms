class Solution:
    def combinationSum(self, candidates : List[int], target: int) -> List[List[int]]:    
        dp = [[] for i in range(target+1)]
        for x in candidates :
            if x <= target:
                dp[x].append([x])  # x is the sum, this cover the only one element case.

            #print(x, x+1, target+1)
            for the_sum in range(x+1, target+1):# x+1 to target(include)
                for lst in dp[the_sum-x]:
                    dp[the_sum].append(lst+[x])
                    
            #for row in dp: print(row)
            #print("-"*20)
        return dp[-1]
                
        
        