class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda a: a[1])

        sorted_queries = sorted((time, i) for i, time in enumerate(queries))

        freq = [0] * (n + 1)
        active = 0
        left = right = 0

        ans = [0] * len(queries)

        for time, idx in sorted_queries:
            start = time - x

            # Add logs within the right boundary
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                if freq[server] == 0:
                    active += 1
                freq[server] += 1
                right += 1

            # Remove logs before the left boundary
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans