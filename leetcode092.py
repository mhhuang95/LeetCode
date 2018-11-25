class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        t = ListNode(-1)
        t.next = head
        left = t
        i = 1
        while i < m:
            left = left.next
            i = i + 1
        l = left.next
        while i < n:
            l = l.next
            i = i + 1
        right = l.next
        r = left.next
        l.next = None
        pre = None
        while r:
            ne = r.next
            r.next = pre
            pre = r
            r = ne
            k = r
        left.next = pre
        k.next = right
        return head

