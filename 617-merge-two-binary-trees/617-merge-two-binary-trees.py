# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        
        def iterate(leftTree, rightTree):
            if not leftTree and not rightTree: 
                return
            v1 = leftTree.val if leftTree else 0 
            v2 = rightTree.val if rightTree else 0 
            node = TreeNode(v1 + v2)
            node.left = iterate(leftTree.left if leftTree else None,rightTree.left if rightTree else None)
            node.right = iterate(leftTree.right if leftTree else None,rightTree.right if rightTree else None)
            return node 
        
        return iterate(root1,root2)