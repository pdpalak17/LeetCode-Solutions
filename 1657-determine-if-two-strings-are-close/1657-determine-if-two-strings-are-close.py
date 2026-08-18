from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        a, b = Counter(word1), Counter(word2)

        return set(a) == set(b) and sorted(a.values()) == sorted(b.values())