class Solution(object):
    def equalPairs(self, grid):
        rows = {}
        for r in grid:
            r = tuple(r)
            rows[r] = rows.get(r, 0) + 1

        ans = 0
        for j in range(len(grid)):
            col = tuple(grid[i][j] for i in range(len(grid)))
            ans += rows.get(col, 0)

        return ans