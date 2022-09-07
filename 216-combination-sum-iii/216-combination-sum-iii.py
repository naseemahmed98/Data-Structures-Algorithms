class Solution(object):
    def combinationSum3(self, k, n):
    
        candidates = list(range(1,10))
        res = []
    
        def dfs(i,curr,total):
            if total == n and len(curr) == k:
                res.append(curr[:])
                return
            
            if i >= len(candidates) or total > n:
                return
            
            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])
            curr.pop()
            dfs(i+1,curr,total)
        
        dfs(0,[],0)
        return res