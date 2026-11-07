class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0

        while n:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or n % 4 == 1:
                n -= 1
                ans += 1
            else:
                n += 1
                ans += 1

        return ans