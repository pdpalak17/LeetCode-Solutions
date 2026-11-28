class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)

        for f, p in items:
            freq[f] += 1

        cnt = [0] * (n + 1)
        for f in range(1, n + 1):
            cnt[f] = sum(freq[j] for j in range(f, n + 1, f)) - 1

        m = min(p for f, p in items)
        arr = sorted((p, cnt[f]) for f, p in items if p < 2 * m)

        ans = budget // m
        cost = copies = 0

        for p, limit in arr:
            take = min(limit, (budget - cost) // p)
            cost += take * p
            copies += take
            ans = max(ans, 2 * copies + (budget - cost) // m)

        return ans