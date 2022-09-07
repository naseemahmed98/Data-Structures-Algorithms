class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        candidates = list(range(1,10))
        res = []
        curr = []

        def backtrack(i, curr, total):
            if total==target and len(curr)==k:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total>target:
                return

            curr.append(candidates[i])
            backtrack(i+1, curr, total+candidates[i])
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0, curr, 0)
        return res