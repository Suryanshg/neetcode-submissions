# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Init pointers to navigate l1 and l2
        ptr1 = l1
        ptr2 = l2

        # Init a new list node and its pointer (for navigation)
        dummy = ListNode()
        ptr = dummy

        # Init with carry value of 0, since we are doing addition 
        # and it requires carry digit
        carry = 0

        # While there is node left to navigate or carry value left
        while ptr1 or ptr2 or carry:

            # Fetch the values of each l1 and l2
            val1 = ptr1.val if ptr1 else 0
            val2 = ptr2.val if ptr2 else 0

            # Add the values of l1 and l2 and carry
            val = val1 + val2 + carry

            # Recalculate carry
            carry = val // 10

            # Calculate the value that can be added (it should be mod 10)
            # This ensures that only digits 0-9 are being used here
            val = val % 10

            # Point the current pointers next to a new list node with the val
            ptr.next = ListNode(val)

            # Move the pointers forward
            ptr = ptr.next
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next

        # Return dummy's next as the actual result LL starts from there
        return dummy.next
