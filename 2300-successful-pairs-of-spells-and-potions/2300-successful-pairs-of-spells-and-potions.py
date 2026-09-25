class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        ans = []

        for s in spells:
            need = (success + s -1)//s

            left, right = 0, m

            while left < right:
                mid = (left + right)// 2

                if potions[mid] >= need:
                    right = mid
                else:
                    left = mid + 1

            ans.append(m - left)

        return ans