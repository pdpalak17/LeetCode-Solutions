from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        L = {}
        s = None
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    s = (i, j)
                elif classroom[i][j] == 'L':
                    L[(i, j)] = k
                    k += 1

        if not k:
            return 0

        full = (1 << k) - 1
        q = deque([(s[0], s[1], energy, 0, 0)])

        # best[x][y][mask] = maximum energy seen
        best = [[{} for _ in range(n)] for _ in range(m)]
        best[s[0]][s[1]][0] = energy

        while q:
            x, y, e, mask, d = q.popleft()

            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                a, b = x + dx, y + dy

                if not (0 <= a < m and 0 <= b < n) or classroom[a][b] == 'X':
                    continue
                if e == 0:
                    continue

                ne = e - 1
                nm = mask

                if (a, b) in L:
                    nm |= 1 << L[(a, b)]

                if nm == full:
                    return d + 1

                if classroom[a][b] == 'R':
                    ne = energy

                if ne > best[a][b].get(nm, -1):
                    best[a][b][nm] = ne
                    q.append((a, b, ne, nm, d + 1))

        return -1