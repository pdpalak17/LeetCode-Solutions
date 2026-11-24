from math import gcd

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            p = g = 0
            l = 1
            for j in range(i, len(nums)):
                x = nums[j]
                p = (p or 1) * x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if p == g * l:
                    ans = max(ans, j - i + 1)
        return ans