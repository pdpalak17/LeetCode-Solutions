class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        from collections import defaultdict

        n = len(items)
        groups = defaultdict(list)

        for i, (f, p) in enumerate(items):
            free = sum(i != j and g % f == 0 for j, (g, _) in enumerate(items))
            if p <= budget:
                groups[p].append(1 + free)

        dp = [-10**9] * (budget + 1)
        dp[0] = 0
        ans = 0

        for p in sorted(groups, reverse=True):
            has = [-10**9] * (budget + 1)

            for v in groups[p]:
                for c in range(budget, p - 1, -1):
                    has[c] = max(has[c], has[c-p] + v, dp[c-p] + v)
                    dp[c] = max(dp[c], dp[c-p] + v)

            for c in range(p, budget + 1):
                if has[c] >= 0:
                    ans = max(ans, has[c] + (budget-c)//p)

        return ans