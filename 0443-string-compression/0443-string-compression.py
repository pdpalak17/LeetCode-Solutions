class Solution:
    def compress(self, chars: List[str]) -> int:
        i = write = 0

        while i < len(chars):
            ch = chars[i]
            count = 0

            while i < len(chars) and chars[i] == ch:
                i += 1
                count += 1

            chars[write] = ch
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write