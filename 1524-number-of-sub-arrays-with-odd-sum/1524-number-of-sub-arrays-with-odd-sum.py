class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd = even = 0
        ans = 0

        for num in arr:
            if num % 2:
                odd, even = even + 1, odd
            else:
                odd, even = odd, even + 1

            ans = (ans + odd) % MOD

        return ans