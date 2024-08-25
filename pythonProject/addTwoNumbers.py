# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l = ListNode()
        l3 = l
        curry = 0
        while (l1 or l2 or curry):
            digit = curry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            curry = digit // 10
            digit = digit % 10
            l3.next = ListNode(digit)

            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            l3 = l3.next
        return l.next





s = Solution()
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)
l2.next.next.next.next  = ListNode(9)
l2.next.next.next.next.next  = ListNode(9)
l2.next.next.next.next.next.next  = ListNode(9)

l3 = s.addTwoNumbers(l2,l1)
while l3 :
    print(l3.val)
    l3 = l3.next