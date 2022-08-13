# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        if not root.left and not root.right:
            return [[root.val]]
        head = root
        res = []
        lst = []
        def findLeaf(node):
        
            if not node:
                return 
            if not node.left and not node.right:
                lst.append(node.val)
                return True 
            if findLeaf(node.left):
                node.left = None
            if findLeaf(node.right):
                node.right = None
           
              
        while root.left or root.right:
            findLeaf(root)
            res.append(lst)
            lst = []
        res.append([root.val])
        return res
        
            
            
        