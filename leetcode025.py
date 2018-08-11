# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        t = []
        l = head
        flag = 1
        p = ListNode(-1)
        p.next = head
        while flag:
            flag, l = self.reverse(l, k)
            p.next = l
            t.append(l)
            if flag:
                for i in range(k):
                    p = l
                    l = l.next

        return t[0]


    def reverse(self, head, k):

        i = 0
        l = head
        while i<k and l != None:
            l = l.next
            i = i + 1
        if i < k:
            return 0, head
        res = head
        temp = head.next
        i = 0
        while i < k-1:
            s = temp
            temp = temp.next
            s.next = res
            res = s
            i = i + 1
        head.next = temp

        return 1,res

def printh(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    s = Solution()
    head = h = ListNode(1)
    for i in range(2,6):
        h.next = ListNode(i)
        h = h.next

    printh(s.reverseKGroup(head,2))


