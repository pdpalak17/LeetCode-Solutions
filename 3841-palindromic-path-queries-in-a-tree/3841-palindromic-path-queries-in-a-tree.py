class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import defaultdict

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS to avoid recursion-depth issues
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = u if p == -1 else p

                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        for j in range(1, LOG):
            for u in range(n):
                parent[j][u] = parent[j - 1][parent[j - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        # Fenwick tree for XOR range updates and point queries
        bit = [0] * (n + 2)

        def add(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def point_query(i):
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        chars = [1 << (ord(c) - ord('a')) for c in s]

        # Subtree range XOR update: toggle a node's contribution
        for u in range(n):
            add(tin[u], chars[u])
            add(tout[u] + 1, chars[u])

        def root_mask(u):
            return point_query(tin[u])

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                delta = chars[u] ^ new_mask

                if delta:
                    add(tin[u], delta)
                    add(tout[u] + 1, delta)
                    chars[u] = new_mask

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                mask = root_mask(u) ^ root_mask(v) ^ chars[w]

                # At most one character may have an odd frequency
                ans.append((mask & (mask - 1)) == 0)

        return ans