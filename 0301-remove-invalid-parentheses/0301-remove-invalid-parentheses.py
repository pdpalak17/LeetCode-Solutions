class Solution(object):
    def removeInvalidParentheses(self, s):
        q = {s}

        while q:
            ans = [x for x in q if self.valid(x)]
            if ans:
                return ans

            q = {
                x[:i] + x[i+1:]
                for x in q
                for i in range(len(x))
                if x[i] in '()'
            }

    def valid(self, s):
        count = 0

        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False

        return count == 0