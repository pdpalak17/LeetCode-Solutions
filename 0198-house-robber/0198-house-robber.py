class Solution:
    def rob(self, nums):
        prev1 = prev2 = 0
        
        for n in nums:
            prev1, prev2 = max(prev1, prev2 + n), prev1
            
        return prev1