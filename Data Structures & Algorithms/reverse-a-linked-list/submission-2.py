# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        ITERATIVE SOLUTION: We maintain two ptrs: Prev and Current
        Prev starts at None, Current starts at head of LL
        At every iteration of LL, we:
        1. Set Current's next as prev (reverse arrow from prev -> curr)
        2. Move Forward (prev to current and current to current.next)
        Return Prev at the end
        '''
        prev = None
        current = head

        while current:
            # Save the current.next for further traversal
            nxt = current.next

            # Set current's next as prev
            # This is reversing the arrow from current to prev
            current.next = prev

            # Move forward
            # Prev becomes current
            prev = current

            # Current moves to nxt
            current = nxt

        # Return the prev ptr
        return prev

