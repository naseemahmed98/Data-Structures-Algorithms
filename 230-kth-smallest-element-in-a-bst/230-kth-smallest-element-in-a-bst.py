# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        node = root
        counter = 0
        while True:
            if node:
                stack.append(node)
                node = node.left 
            else:
                node = stack.pop()
                counter += 1 
                if counter == k:
                    break
                node = node.right
        return node.val

        