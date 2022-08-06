class Solution:
    def subArrayRanges(self, nums):
        minsum = maxsum = 0
        stack = []
        for x in range(len(nums)+1):
            while stack and (x == len(nums) or nums[stack[-1]] > nums[x]):
                i = stack.pop()
                if stack:
                    prev_smaller = stack[-1]
                else:
                    prev_smaller = -1
                minsum += nums[i] * (x - i) * (i - prev_smaller)
            stack.append(x)
        stack = []
        for x in range(len(nums) + 1):
            while stack and (x == len(nums) or nums[stack[-1]] < nums[x]):
                i = stack.pop()
                if stack:
                    prev_larger = stack[-1]  
                else:
                    prev_larger = -1
                maxsum += nums[i] * (x - i) * (i - prev_larger)
            stack.append(x)
        
        return maxsum - minsum