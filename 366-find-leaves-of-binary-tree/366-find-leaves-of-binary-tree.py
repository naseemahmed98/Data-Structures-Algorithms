# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        
        def getHeight(node):
            if not node:
                return -1 
            height = max(getHeight(node.left),getHeight(node.right)) + 1 
            if height >= len(result):
                result.append([])
            
            result[height].append(node.val)
            return height
        result = []
        height_of_root = getHeight(root)
        return result
            
            
        