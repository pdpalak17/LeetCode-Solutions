from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        a = sorted((r, l, w, i) for i, (l, r, w) in enumerate(intervals))
        ends = [x[0] for x in a]
        n = len(a)

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i, (r, l, w, idx) in enumerate(a, 1):
            p = bisect_left(ends, l, 0, i - 1)

            for k in range(1, 5):
                x = dp[i - 1][k]
                y = dp[p][k - 1]
                take = (y[0] + w, tuple(sorted(y[1] + (idx,))))

                dp[i][k] = x if x[0] > take[0] or (x[0] == take[0] and x[1] < take[1]) else take

        return list(dp[n][4][1])