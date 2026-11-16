class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = ""
            for i in range(0, len(s), k):
                total = sum(int(c) for c in s[i:i+k])
                res += str(total)
            s = res

        return s