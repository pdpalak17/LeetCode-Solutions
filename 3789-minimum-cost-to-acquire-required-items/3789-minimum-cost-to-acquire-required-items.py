class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        both = min(need1, need2)

        return min(
            both * costBoth + (need1 - both) * cost1 + (need2 - both) * cost2,
            max(need1, need2) * costBoth,
            need1 * cost1 + need2 * cost2
        )