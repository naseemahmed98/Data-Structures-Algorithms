class Solution(object):
    def combinationSum(self, candidates, target):
        res= []

        
        def backTrack(i,curr,total):
            if total == target:
                res.append(curr[:])
                return
            if i == len(candidates) or total > target:
                return
            curr.append(candidates[i])
            backTrack(i,curr,total+candidates[i])
            curr.pop()
            backTrack(i+1,curr,total)
        
        backTrack(0,[],0)
        return res