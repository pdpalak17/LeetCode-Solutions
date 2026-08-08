class Solution:
    def largestAltitude(self, gain):
        max_alt = 0  # starts at altitude 0
        current = 0

        for g in gain:
            current += g
            max_alt = max(max_alt, current)

        return max_alt