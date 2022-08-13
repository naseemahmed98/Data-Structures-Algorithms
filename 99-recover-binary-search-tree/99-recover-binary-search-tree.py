# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        self.previous_node = TreeNode(float("-inf"))
        self.switch_one, self.switch_two = None, None 
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if not self.switch_one and node.val < self.previous_node.val:
                self.switch_one = self.previous_node
            if self.switch_one and node.val < self.previous_node.val:
                self.switch_two = node
            self.previous_node = node 
            inorder(node.right)
        
        inorder(root)
        self.switch_one.val, self.switch_two.val = self.switch_two.val,self.switch_one.val
        
            
        