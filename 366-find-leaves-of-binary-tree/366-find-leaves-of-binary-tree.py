# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
      
        res = []
        def iterate(node):
            if not node.left and not node.right:
                temp.append(node.val)
                return True
            if node.left:
                if iterate(node.left):
                    node.left = None
                
            if node.right:
                if iterate(node.right):
                    node.right = None
            
        
        while root.left or root.right:
            temp = []
            iterate(root)
            res.append(temp)
        
        res.append([root.val])
        return res
        