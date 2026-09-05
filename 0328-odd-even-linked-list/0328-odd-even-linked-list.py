class Solution:
    def oddEvenList(self, head):
        if not head:
            return head

        odd  = head
        even = head.next
        even_head = even      # save even's start to attach at end

        while even and even.next:
            odd.next  = even.next   # odd → next odd
            odd       = odd.next
            even.next = odd.next    # even → next even
            even      = even.next

        odd.next = even_head        # connect odd tail to even head
        return head