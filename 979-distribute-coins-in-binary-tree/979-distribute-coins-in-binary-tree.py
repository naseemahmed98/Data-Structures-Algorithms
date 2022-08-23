# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root):
        
        self.steps = 0
        
        def coins(curr):
            if not curr:
                return 0
            
            left_coins = coins(curr.left)
            right_coins = coins(curr.right)
            self.steps += abs(left_coins) + abs(right_coins)

            return (left_coins + right_coins + curr.val) - 1
            
        
        coins(root)
        
        return self.steps
           