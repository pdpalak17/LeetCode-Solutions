class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        max_diff = max(diff)
        freq = [0] * (max_diff + 1)

        for d in diff:
            freq[d] += 1

        for d in range(max_diff, 0, -1):
            if k == 0:
                break

            move = min(freq[d], k)
            freq[d] -= move
            freq[d - 1] += move
            k -= move

        return sum(d * d * count for d, count in enumerate(freq))