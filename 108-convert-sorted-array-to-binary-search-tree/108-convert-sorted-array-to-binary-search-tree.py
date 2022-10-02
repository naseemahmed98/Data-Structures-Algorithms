# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        
        
        def constructTree(array):
            if not array:
                return 
            median = len(array) // 2 
            node = TreeNode(array[median])
            node.left = constructTree(array[:median])
            node.right = constructTree(array[median+1:])
            return node
        
        return constructTree(nums)