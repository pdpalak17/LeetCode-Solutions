from collections import defaultdict, deque
class Solution:
    def remainingMethods(self, n, k, invocations):
        g = defaultdict(list)
        for u, v in invocations:
            g[u].append(v)
        s = {k}
        q = deque([k])
        while q:
            u = q.popleft()
            for v in g[u]:
                if v not in s:
                    s.add(v)
                    q.append(v)
        for u, v in invocations:
            if u not in s and v in s:
                return list(range(n))
        return [i for i in range(n) if i not in s]