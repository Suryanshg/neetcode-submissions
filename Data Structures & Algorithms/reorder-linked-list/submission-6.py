# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. Divide list into two parts by their midpoint (midpoint remains in first half in case of odd len)
        #2. Reverse the second list
        #3. Merge elements into each other in order, starting from first, until there are elements in the second list

        #1. 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        #2. l2 starts at slow.next
        cur = slow.next
        prev = None

        slow.next = None # End l1 at None which splits the list

        # Reverse the second list
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # 3.
        l1 = head
        l2 = prev
        while l2:
            nxt1 = l1.next
            nxt2 = l2.next
            l1.next = l2
            l2.next = nxt1
            l1 = nxt1
            l2 = nxt2
