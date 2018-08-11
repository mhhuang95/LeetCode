# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        res = h = ListNode(-1)
        h.next = head
        while head != None:
            l2 = head
            head = head.next
            if head == None:
                return res.next
            l1 = head
            head = head.next
            h.next = l1
            l1.next = l2
            l2.next = head
            h = l2
        return res.next

