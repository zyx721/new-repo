# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getlength(self,head):
        cur = head
        v=0
        while cur :
            v+=1
            cur=cur.next
        return v
    def print(self,cur):
        head = cur
        while head:
            print(head.val)
            head = head.next
    def removeNthFromEnd(self, head, n):
        if head:
            v = self.getlength(head)
            if v == 1:
                head =  None
                return head
            if n == 1:
                cur = head
                while cur:
                    if cur.next.next is None:
                        cur.next = None
                        return head
                    cur = cur.next
            if n == v:
                head = head.next
                return head
            else:
                cur = head
                for i in range(1,v-n+1):
                    k = cur
                    cur = cur.next
                cur = None
                k.next=k.next.next
                return head
s= Solution()
l = ListNode(1)
l.next=ListNode(2)
l.next.next=ListNode(3)
l.next.next.next=ListNode(4)
l.next.next.next.next=ListNode(5)

s.print(l)
l = s.removeNthFromEnd(l,2)
s.print(l)