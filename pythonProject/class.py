class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        return head.next

# Create linked lists list1 and list2
list1 = ListNode(1)
list1.next = ListNode(3)


list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

# Create an instance of Solution class
sol = Solution()

# Merge list1 and list2
merged_list = sol.mergeTwoLists(list1, list2)

# Print the merged list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
