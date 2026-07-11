# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Start slow and fast ptr at same position
        slow, fast = head, head
        
        # Since we shift fast by 2, we check if fast and fast.next exists
        while fast and fast.next:

            # Move slow by 1 and fast by 2
            slow = slow.next
            fast = fast.next.next

            # If they meet, return true
            if slow == fast:
                return True

        # Return false as default case
        return False
        