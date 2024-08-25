# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        cur = head
        n=0
        while cur and cur.next:
            if n % 2 == 0:
                k = cur
                cur.next = cur.next.next
                cur.next.next = k
                print(cur.val)
            cur = cur.next
            n+=1
        return head

s = Solution()
l = ListNode(1)
l.next=ListNode(2)
l.next.next=ListNode(3)
l.next.next.next=ListNode(4)
l.next.next.next.next=ListNode(5)
l.next.next.next.next.next=ListNode(6)

s.swapPairs(l)
s.pri(l)



