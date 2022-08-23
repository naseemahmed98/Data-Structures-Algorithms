# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root):
        
        self.moves = 0 
        
        def countCoins(node):
            if not node:
                return 0
            leftCount = countCoins(node.left)
            rightCount = countCoins(node.right)
            self.moves += abs(leftCount) + abs(rightCount)
            return (leftCount + rightCount + node.val) - 1 
        
        countCoins(root)
        return self.moves
            
            