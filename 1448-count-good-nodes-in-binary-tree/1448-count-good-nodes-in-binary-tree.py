class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maximum):
            if not node:
                return 0
            
            count = 0
            
            if node.val >= maximum:
                count = 1
                maximum = node.val
            
            return count + dfs(node.left, maximum) + dfs(node.right, maximum)
        
        return dfs(root, root.val)