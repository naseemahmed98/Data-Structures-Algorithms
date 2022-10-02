# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        self.res = None
        
        def iterate(node):
            if not node:
                return False
            left = iterate(node.left)
            right = iterate(node.right)
            curr = (node.val == p.val) or (node.val == q.val)
            if (left and right) or (left and curr) or (right and curr):
                self.res = node

            return curr or left or right
        
        iterate(root)
        return self.res
            