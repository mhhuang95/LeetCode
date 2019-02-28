# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ls = len(lists)
        if ls == 0:
            return None
        res = lists[0]
        for i in range(ls-1):
            res = self.mergeTwoLists(res, lists[i+1])
        return res



    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = head = ListNode(-1)
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                h.next = l2
                h = h.next
                l2 = l2.next
            else:
                h.next = l1
                h = h.next
                l1 = l1.next
        if l1 !=None:
            h.next = l1
        if l2 != None:
            h.next = l2
        return head.next