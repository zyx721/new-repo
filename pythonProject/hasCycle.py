# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        l = []
        if head:
            cur = head
            while cur.next:
                if cur.next in l:
                    return True
                l.append(cur.next)
                cur = cur.next
        return False

v = ListNode(3)
v.next = ListNode(2)
v.next.next= ListNode(0)
v.next.next.next= ListNode(-4)
v.next.next.next.next= ListNode(2)
s = Solution()
print(s.hasCycle(v))