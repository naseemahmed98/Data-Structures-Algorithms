# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
         
        
        def traverse(leftTree, rightTree):
            if not leftTree and not rightTree:
                return True 
            if (not leftTree or not rightTree) or (leftTree.val != rightTree.val):
                return False 
            return traverse(leftTree.left,rightTree.right) and traverse(leftTree.right,rightTree.left)
        
        return traverse(root,root)
            
      