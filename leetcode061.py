# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        curr = head
        ls = 1
        while curr.next != None:
            curr = curr.next
            ls += 1
        k = k % ls
        if k == 0:
            return head
        curr = head
        t = ls-k-1
        while t > 0:
            curr = curr.next
            t -= 1
        l = curr.next
        curr.next = None
        curr = l
        while curr.next != None:
            curr = curr.next
        curr.next = head
        head = l
        return head