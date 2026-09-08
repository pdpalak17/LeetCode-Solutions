class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def leaves(root):
            if not root:
                return []
            
            if not root.left and not root.right:
                return [root.val]
            
            return leaves(root.left) + leaves(root.right)
        
        return leaves(root1) == leaves(root2)