class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                best = length

                for d in range(1, length):
                    if length % d:
                        continue

                    changes = 0
                    for j in range(d):
                        a, b = l + j, l + j + ((length - 1 - j) // d) * d

                        while a < b:
                            if s[a] != s[b]:
                                changes += 1
                            a += d
                            b -= d

                    best = min(best, changes)

                cost[l][l + length - 1] = best

        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):
                for j in range(2 * (parts - 1), i - 1):
                    dp[parts][i] = min(
                        dp[parts][i],
                        dp[parts - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]