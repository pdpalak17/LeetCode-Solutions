class Solution:
    def pairSum(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return max(x + y for x, y in zip(a, a[::-1]))