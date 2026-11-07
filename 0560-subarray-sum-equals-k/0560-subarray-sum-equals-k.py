class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            count += freq.get(curr_sum - k, 0)

            freq[curr_sum] = freq.get(curr_sum, 0) + 1

        return count