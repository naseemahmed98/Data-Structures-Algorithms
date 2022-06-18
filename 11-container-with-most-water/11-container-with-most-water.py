class Solution(object):
    def maxArea(self, lst):
        max_area = 0
        l, r = 0, len(lst)-1
        while l < r:
            max_area = max(max_area,min(lst[l], lst[r]) * (r - l ))
            if lst[l] >= lst[r]:
                r -= 1
            elif lst[r] > lst[l]:
                l += 1

        return max_area
