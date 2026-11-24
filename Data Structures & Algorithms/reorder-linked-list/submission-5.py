# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find midpoint
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # Reverse Second list
        cur, prev = slow.next, None
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # Combine both
        l1 = head
        l2 = prev
        while l2:
            nxt1, nxt2 = l1.next, l2.next
            l1.next = l2
            l2.next = nxt1
            l1 = nxt1
            l2 = nxt2

