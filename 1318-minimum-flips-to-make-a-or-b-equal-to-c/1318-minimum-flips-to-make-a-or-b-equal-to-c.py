class Solution:
    def minFlips(self, a, b, c):
        ans = 0

        while a or b or c:
            x = a & 1
            y = b & 1
            z = c & 1

            if z == 1:
                if x == 0 and y == 0:
                    ans += 1
            else:
                ans += x + y

            a >>= 1
            b >>= 1
            c >>= 1

        return ans