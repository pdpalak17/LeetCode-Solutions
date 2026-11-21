class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        ans = [1] * n
        last = {}

        def dfs(u):
            old = last.get(s[u], -1)
            last[s[u]] = u

            for v in children[u]:
                dfs(v)

            p = old if old != -1 else parent[u]
            if u:
                ans[p] += ans[u]

            if old == -1:
                last.pop(s[u], None)
            else:
                last[s[u]] = old

        dfs(0)
        return ans