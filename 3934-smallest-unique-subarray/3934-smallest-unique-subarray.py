class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        a = [x + 1 for x in nums] + [0]
        N = n + 1

        p = sorted(range(N), key=lambda i: a[i])
        c = [0] * N

        for i in range(1, N):
            c[p[i]] = c[p[i-1]] + (a[p[i]] != a[p[i-1]])

        k = 1
        while k < N:
            pn = [(x-k) % N for x in p]
            cnt = [0] * N
            for x in c:
                cnt[x] += 1
            for i in range(1, N):
                cnt[i] += cnt[i-1]

            for x in reversed(pn):
                cnt[c[x]] -= 1
                p[cnt[c[x]]] = x

            cn = [0] * N
            for i in range(1, N):
                x, y = p[i-1], p[i]
                cn[y] = cn[x] + (
                    (c[y], c[(y+k) % N]) !=
                    (c[x], c[(x+k) % N])
                )
            c = cn
            k *= 2

        sa = p[1:]
        rank = [0] * n
        for i, x in enumerate(sa):
            rank[x] = i

        lcp = [0] * n
        h = 0
        for i in range(n):
            r = rank[i]
            if r == 0:
                h = 0
                continue
            j = sa[r-1]
            while i+h < n and j+h < n and nums[i+h] == nums[j+h]:
                h += 1
            lcp[r] = h
            h = max(0, h-1)

        ans = n
        for r in range(n):
            length = max(lcp[r], lcp[r+1] if r+1 < n else 0) + 1
            if length <= n - sa[r]:
                ans = min(ans, length)

        return ans