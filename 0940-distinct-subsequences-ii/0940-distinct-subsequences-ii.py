class Solution:
    def distinctSubseqII(self, s):
        dp = 1
        last = {}

        for c in s:
            new = dp * 2 - last.get(c, 0)
            last[c] = dp
            dp = new % (10**9 + 7)

        return (dp - 1) % (10**9 + 7)