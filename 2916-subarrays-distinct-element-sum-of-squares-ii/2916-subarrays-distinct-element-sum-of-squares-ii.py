class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        s = [0] * size
        sq = [0] * size
        lazy = [0] * size

        def apply(node, left, right, v):
            length = right - left + 1
            sq[node] = (sq[node] + 2 * v * s[node] + v * v * length) % MOD
            s[node] = (s[node] + v * length) % MOD
            lazy[node] += v

        def push(node, left, right):
            if lazy[node] and left != right:
                mid = (left + right) // 2
                apply(node * 2, left, mid, lazy[node])
                apply(node * 2 + 1, mid + 1, right, lazy[node])
                lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return
            push(node, left, right)
            mid = (left + right) // 2
            if ql <= mid:
                update(node * 2, left, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)
            s[node] = (s[node * 2] + s[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i)
            last[x] = i
            ans = (ans + sq[1]) % MOD

        return ans