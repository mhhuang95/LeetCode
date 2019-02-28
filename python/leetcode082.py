# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        temp = ListNode(-1)
        temp.next = head

        pos = temp
        last = head
        flag = 0

        while last:
            flag = 0
            while last.next != None and last.val == last.next.val:
                flag = 1
                last.next = last.next.next

            if flag:
                pos.next = last.next
            else:
                pos=last

            last = last.next

        return temp.next


