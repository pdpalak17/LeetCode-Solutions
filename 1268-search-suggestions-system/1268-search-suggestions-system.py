class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        ans = []
        prefix = ""

        for c in searchWord:
            prefix += c
            ans.append([x for x in products if x.startswith(prefix)][:3])

        return ans