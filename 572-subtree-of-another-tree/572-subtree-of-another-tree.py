# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def iterate(root, subRoot):
            if root:
                if compare_node(root, subRoot):
                    return True
                return iterate(root.left, subRoot) or iterate(root.right, subRoot)
            return False
        
        
        def compare_node(r,s):
            if not r and not s:
                return True
            
            if not r or not s:
                return False
            
            if r and s:
                if r.val != s.val:
                    return False
        
                if r.val == s.val:
                    return compare_node(r.left, s.left) and compare_node(r.right, s.right)
        return iterate(root,subRoot)
    
    
    
    
