class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        curttun = head
        while curttun.next :
            if curttun.val == curttun.next.val :
                curttun.next =curttun.next.next
            else:
                curttun = curttun.next
        return head
