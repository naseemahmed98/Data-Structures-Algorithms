class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root.left and not root.right:
            return [root.val]
        
        
        def traverseBoundary(node, boundaryPath, isLeft):
            if not node:
                return 
            
            if isLeft:
                if node.left:
                    boundaryPath.append(node.val)
                    traverseBoundary(node.left,boundaryPath,isLeft)
                elif node.right:
                    boundaryPath.append(node.val)
                    traverseBoundary(node.right,boundaryPath,isLeft)
            
            else:
                if node.right:
                    boundaryPath.append(node.val)
                    traverseBoundary(node.right,boundaryPath,isLeft)
                elif node.left:
                    boundaryPath.append(node.val)
                    traverseBoundary(node.left,boundaryPath,isLeft)
        
        def getLeaves(node):
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.left:
                getLeaves(node.left)
            if node.right:
                getLeaves(node.right)
        
        
        left,right,leaves = [root.val],[],[]
        traverseBoundary(root.left,left,True)
        traverseBoundary(root.right,right,False)
        getLeaves(root)
        return left + leaves + list(reversed(right))
        
                    