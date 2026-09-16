class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = [False]*n
        visited[0] = True
        stack = [0]
        changes = 0

        while stack:
            city = stack.pop()

            for neighbor, cost in graph[city]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    changes += cost
                    stack.append(neighbor)

        return changes