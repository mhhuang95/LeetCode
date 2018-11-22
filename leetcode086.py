# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return head
        part1 = ListNode(-1)
        p1 = part1
        part2 = ListNode(-1)
        p2 = part2
        while head != None:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p2.next = None
        p1.next = part2.next
        return part1.next

def print_l(head):
    while head != None:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    head = ListNode(1)
    p = head
    p.next = ListNode(4)
    p = p.next
    p.next = ListNode(3)
    p = p.next
    p.next = ListNode(2)
    p = p.next
    p.next = ListNode(5)
    p = p.next
    p.next = ListNode(2)
    s = Solution()
    print_l(s.partition(head,3))