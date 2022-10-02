# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        self.res = None
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            curr = (node == p) or (node == q)
            if (left and curr) or (left and right) or (right and curr):
                self.res = node 
                #return True
            return left or right or curr 
        
        dfs(root)
        return self.res