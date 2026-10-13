class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted((x * x for x in nums), reverse = True)
        mid = (len(nums) + 1) // 2
        return sum(squares[:mid]) - sum(squares[mid:])