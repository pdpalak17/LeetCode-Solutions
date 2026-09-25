class Solution:
    def braceExpansionII(self, expression):
        n = len(expression)

        def parse(i):
            res = {""}
            total = set()

            while i < n and expression[i] != '}':
                if expression[i] == ',':
                    total |= res
                    res = {""}
                    i += 1

                elif expression[i] == '{':
                    part, i = parse(i + 1)
                    res = {a + b for a in res for b in part}

                else:
                    res = {a + expression[i] for a in res}
                    i += 1

            total |= res
            return total, i + 1

        ans, _ = parse(0)
        return sorted(ans)