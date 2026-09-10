class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = {0: 1}

        def dfs(node, current):
            if not node:
                return 0

            current += node.val

            ans = count.get(current - targetSum, 0)

            count[current] = count.get(current, 0) + 1

            ans += dfs(node.left, current)
            ans += dfs(node.right, current)

            count[current] -= 1

            return ans

        return dfs(root, 0)