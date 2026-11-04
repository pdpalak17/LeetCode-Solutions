class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if (r < 0 or r >= m or c < 0 or c >= n
                    or grid[r][c] == '0'):
                return

            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count