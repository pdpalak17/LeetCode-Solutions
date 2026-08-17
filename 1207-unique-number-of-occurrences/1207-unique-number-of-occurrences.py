class Solution(object):
    def uniqueOccurrences(self, arr):
        d = {}
        for x in arr:
            d[x] = d.get(x, 0) + 1

        return len(d.values()) == len(set(d.values()))