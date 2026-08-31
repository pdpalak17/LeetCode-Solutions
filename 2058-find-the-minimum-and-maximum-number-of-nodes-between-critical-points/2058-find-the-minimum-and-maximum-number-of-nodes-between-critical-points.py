class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        cur = head.next
        pos = 1
        first = last = -1
        mn = float('inf')

        while cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or \
               (cur.val < prev.val and cur.val < cur.next.val):

                if first != -1:
                    mn = min(mn, pos - last)
                else:
                    first = pos

                last = pos

            prev = cur
            cur = cur.next
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [mn, last - first]