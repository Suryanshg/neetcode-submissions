# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Partition into the LL into two
        # using slow and fast ptr technique
        # slow begins at head, fast begins at head.next
        # at the end, slow will be at the half way position
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Partition 2 starts with slow.next
        part2 = slow.next  

        # Since slow (last element of part1) will be pointing to Null in the end
        slow.next = None

        # Reverse part2
        prev = None
        curr = part2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Now part2 is reversed and stored in prev
        part1, part2 = head, prev

        # Combine part1 and part2 one by one
        while part2:
            # Save next of part1 and part2
            part1_next, part2_next = part1.next, part2.next
            
            # Point part1's next to part2
            # Point part2's next to part1's old next
            part1.next = part2
            part2.next = part1_next

            # Move part1 and part2 forward
            part1, part2 = part1_next, part2_next

        


        

        

        
