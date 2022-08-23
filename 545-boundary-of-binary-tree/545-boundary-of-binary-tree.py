class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root.left and not root.right:
            return [root.val]
        
        
        def dfs(node, arr, is_right):
            
            if not node:
                return 
            
            if not node.left and not node.right:
                return 
            
            arr.append(node.val)
            if is_right:
                if node.right:
                    dfs(node.right, arr, is_right)

                else:
                    dfs(node.left, arr, is_right)
            else:
                if node.left:
                    dfs(node.left, arr, is_right)
                else:
                    dfs(node.right, arr, is_right)
                    
        def find_leaf(node):
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            if node.left:
                find_leaf(node.left)
                
            if node.right:
                find_leaf(node.right)
                
                
        
        
        right = []
        dfs(root.right, right, True)
        left = []
        dfs(root.left, left, False)
        leaves = []
        find_leaf(root)
            
        
        return [root.val] + left + leaves + list(reversed(right))