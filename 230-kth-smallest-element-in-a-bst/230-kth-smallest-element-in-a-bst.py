# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        self.counter = 0
        def kth(node):
            if not node:
                return 
            kth(node.left)
            self.counter += 1
            
            if self.counter == k:
                self.kth_Smallest = node.val
            
            kth(node.right)
        kth(root)
        return self.kth_Smallest


        