class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        from collections import deque

        m,n = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            r,c,d = q.popleft()

            for nr, nc in ((r+1, c), (r-1,c), (r, c+1), (r, c-1)):
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    if nr == 0 or nr == m-1 or nc == 0 or nc == n-1:
                        return d + 1
                    maze[nr][nc] = '+'
                    q.append((nr, nc, d+1))

        return - 1