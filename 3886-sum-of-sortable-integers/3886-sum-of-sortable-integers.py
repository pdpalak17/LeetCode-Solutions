class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        def is_rotation(block, target_block):
            m = len(block)

            if block == target_block:
                return True

            pattern = target_block
            pi = [0] * m
            j = 0

            for i in range(1, m):
                while j and pattern[i] != pattern[j]:
                    j = pi[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j

            j = 0
            doubled = block + block[:-1]

            for x in doubled:
                while j and x != pattern[j]:
                    j = pi[j - 1]
                if x == pattern[j]:
                    j += 1
                if j == m:
                    return True

            return False

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                target_block = target[start:start + k]

                if not is_rotation(block, target_block):
                    valid = False
                    break

            if valid:
                ans += k

        return ans