# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            # Save the current.next for further traversal
            temp = current.next

            # Set current's next to be previous node
            current.next = prev

            # Set previous node to be current
            prev = current

            # Move current to its next (saved in temp)
            current = temp

        # Return the prev ptr
        return prev

# None-> 1 -> 2 -> 3 -> None
# 1 -> None, next: 2 -> 3 -> None
# 2 -> 1 -> None , next: 3 -> None
# ...

