class Solution:
    def decodeString(self, s):
        stack   = []
        current = ""
        k       = 0

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)        # build multi-digit number

            elif ch == '[':
                stack.append((current, k))  # save state
                current = ""
                k       = 0

            elif ch == ']':
                prev_str, repeat = stack.pop()
                current = prev_str + current * repeat

            else:
                current += ch               # regular character

        return current