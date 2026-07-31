from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        for i, f in enumerate(sorted(Counter(word).values(), reverse=True)):
            ans += f * (i // 8 + 1)
        return ans