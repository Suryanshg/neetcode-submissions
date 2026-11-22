# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Slow and Fast ptrs to find the midpoint
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        # Reverse l2
        dummy = prev = None
        cur = l2
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        l2 = prev
        l1 = head

        # print(l2.val, l2.next)
    
        while l1 and l2:
            if l2:
                l2_next = l2.next
            l1_next = l1.next
            l1.next = l2
            if l2:
                l2.next = l1_next

            # Move forward
            l1 = l1_next
            l2 = l2_next
        


        


