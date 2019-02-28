class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def addTwoNumbers(self, l1, l2):
        d = 0
        l3 = head = ListNode(-1)
        while l1 != None and l2 != None:
            temp = l1.val + l2.val
            l3.next = ListNode(temp)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        if l1 != None:
            l3.next = l1
        if l2 != None:
            l3.next = l2
        l3 = head.next
        while l3 != None:
            l3.val = l3.val + d
            d = 0
            if l3.val >= 10:
                d = 1
                l3.val = l3.val - 10
            t = l3
            l3 = l3.next
        if d == 1:
            t.next = ListNode(1)
        return head.next
