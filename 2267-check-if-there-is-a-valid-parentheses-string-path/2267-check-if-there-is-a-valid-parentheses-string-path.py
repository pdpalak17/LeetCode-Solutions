class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = 2
                    continue

                reachable = dp[j]

                if j > 0:
                    reachable |= dp[j - 1]

                if grid[i][j] == '(':
                    dp[j] = reachable << 1
                else:
                    dp[j] = reachable >> 1

                remaining = (m - 1 - i) + (n - 1 - j)

                if remaining >= 0:
                    dp[j] &= (1 << (remaining + 1)) - 1

        return (dp[n - 1] & 1) != 0