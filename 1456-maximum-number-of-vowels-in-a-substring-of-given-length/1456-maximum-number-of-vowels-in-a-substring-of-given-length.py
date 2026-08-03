class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = set("aeiou")
        cur = ans = sum(c in v for c in s[:k])

        for i in range(k, len(s)):
            cur += s[i] in v
            cur -= s[i-k] in v
            ans = max(ans, cur)

        return ans