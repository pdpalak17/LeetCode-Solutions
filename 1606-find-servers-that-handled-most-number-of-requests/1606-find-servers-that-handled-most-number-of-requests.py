import heapq
from bisect import bisect_left

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            # Release servers that have finished their requests
            while busy and busy[0][0] <= time:
                end_time, server = heapq.heappop(busy)

                # Insert server back in sorted order
                import bisect
                bisect.insort(available, server)

            if not available:
                continue

            # Find the next available server
            idx = bisect_left(available, i % k)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            count[server] += 1
            heapq.heappush(busy, (time + load[i], server))

        max_count = max(count)

        return [i for i in range(k) if count[i] == max_count]