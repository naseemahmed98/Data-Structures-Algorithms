# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        self.prev = TreeNode(float("-inf"))
        self.switchOne, self.switchTwo = None, None 
        
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if not self.switchOne and node.val < self.prev.val:
                self.switchOne = self.prev 
            if node.val < self.prev.val:
                self.switchTwo = node
            self.prev = node
            inorder(node.right)
        
        inorder(root)
        self.switchOne.val,self.switchTwo.val = self.switchTwo.val, self.switchOne.val
