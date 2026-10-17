class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)

        sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))

        pos = {num: i for i, num in enumerate(sorted_nums)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[nums[i]] == i:
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle += 1

            swaps += cycle - 1

        return swaps