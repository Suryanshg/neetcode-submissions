# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node and init left ptr there
        # right starts at head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right away from left n times
        i = 0
        while i < n:
            right = right.next
            i += 1

        # Now that left and right are n steps away, move right ptr forward
        while right:
            left = left.next
            right = right.next

        # left will be the node before the one to be removed
        # so now we remove it
        left.next = left.next.next
        return dummy.next

        