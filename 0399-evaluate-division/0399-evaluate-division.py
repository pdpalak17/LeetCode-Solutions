class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict, deque

        graph = defaultdict(list)

        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def bfs(a, b):
            q = deque([(a, 1.0)])
            seen = {a}

            while q:
                x, value = q.popleft()
                if x == b:
                    return value

                for y, weight in graph[x]:
                    if y not in seen:
                        seen.add(y)
                        q.append((y, value * weight))

            return -1.0

        return [bfs(a, b) if a in graph and b in graph else -1.0 for a, b in queries]