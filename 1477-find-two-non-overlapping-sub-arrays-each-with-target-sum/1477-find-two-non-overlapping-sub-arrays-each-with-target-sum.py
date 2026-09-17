class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')]*(n + 1)
        left = total = 0
        ans = float('inf')

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            best[right + 1] = best[right]

            if total == target:
                length = right - left + 1
                ans = min(ans, length + best[left])
                best[right + 1] = min(best[right + 1], length)

        return - 1 if ans == float('inf') else ans