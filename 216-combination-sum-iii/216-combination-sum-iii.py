class Solution(object):
    def combinationSum3(self, k, n):
        dp = [set() for x in range(n + 1)]
        print(dp)
        dp[0].add(())
        print(dp)
        characters = [i for i in range(1, 10)]

        for char_num in characters:
            for num_range in range(n, char_num -1, -1):
                for prev in dp[num_range - char_num]:
                    current_val = prev + (char_num,)
                    dp[num_range].add(current_val)
        res = []
        
        for each in dp[-1]:
            if len(each) == k:
                res.append(each)
        return res
                        