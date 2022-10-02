# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        if not root:
            return 
        self.newRoot = None 
        def iterate(parent,child):
            if not child:
                self.newRoot = parent 
                return True 
            if iterate(child,child.left):
                child.left = parent.right if parent else None
                child.right = parent
                return True
           
            
        
        
        iterate(None, root)
        return self.newRoot