class Solution(object):
    def largestInteger(self, nums, k):
        count = {}
        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i+k]):
                count[x] = count.get(x, 0) + 1
        ans = [x for x in count if count[x] == 1]
        return max(ans) if ans else -1