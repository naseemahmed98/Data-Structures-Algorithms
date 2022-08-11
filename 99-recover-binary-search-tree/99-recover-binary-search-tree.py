# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        
        self.p1 = None
        self.p2 = None
        self.pre = TreeNode(float('-inf'))
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if not self.p1 and node.val<self.pre.val:
                self.p1 = self.pre
            if self.p1 and node.val<self.pre.val:
                self.p2 = node
            self.pre = node
            dfs(node.right)
        dfs(root)
        self.p1.val,self.p2.val = self.p2.val,self.p1.val
        
        
        
