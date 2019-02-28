class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ls = 0
        t = head
        while t is not None:
            t = t.next
            ls = ls + 1
        k = ls - n
        if k == 0:
            return head.next
        t = head
        for i in range(k-1):
            t = t.next
        l = t.next
        if l == None:
            return None
        elif l.next== None:
            t.next = None
        else:
            t.next = l.next
        return head

    def printh(self, head):
        while head is not None:
            print(head.val)
            head = head.next

if __name__=="__main__":
    h =head = ListNode(1)

    s = Solution()
    t = s.removeNthFromEnd(h,1)
    s.printh(t)