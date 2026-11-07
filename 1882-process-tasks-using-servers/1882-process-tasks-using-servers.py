import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            # Release all servers that have become free
            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, jump to the next free time
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Assign the task
            weight, index = heapq.heappop(available)
            ans.append(index)

            heapq.heappush(busy, (time + duration, weight, index))

        return ans