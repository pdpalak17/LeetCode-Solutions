class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        sums = []

        def dfs(node):
            if not node:
                return 0

            total = node.val
            total += dfs(node.left)
            total += dfs(node.right)

            sums.append(total)
            return total

        total_sum = dfs(root)

        max_product = 0

        for sub_sum in sums:
            product = sub_sum * (total_sum - sub_sum)
            max_product = max(max_product, product)

        return max_product % MOD