# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0, head)
        left = prev
        right = head

        i = 0
        while i < n:
            right = right.next
            i += 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return prev.next

        