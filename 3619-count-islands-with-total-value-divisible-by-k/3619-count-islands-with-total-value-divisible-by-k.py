class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    stack = [(i, j)]
                    visited[i][j] = True
                    total = 0

                    while stack:
                        r, c = stack.pop()
                        total += grid[r][c]

                        for nr, nc in (
                            (r - 1, c), (r + 1, c),
                            (r, c - 1), (r, c + 1)
                        ):
                            if (0 <= nr < m and 0 <= nc < n
                                    and grid[nr][nc] > 0
                                    and not visited[nr][nc]):
                                visited[nr][nc] = True
                                stack.append((nr, nc))

                    if total % k == 0:
                        count += 1

        return count