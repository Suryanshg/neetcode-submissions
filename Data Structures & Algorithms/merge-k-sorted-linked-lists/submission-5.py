# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        min_heap = []
        i = 0
        for l in lists:
            while l:
                heapq.heappush(min_heap, (l.val, i, l))
                l = l.next
                i+=1 
        
        dummy = ListNode(0)
        head = dummy

        while min_heap:
            _, _, l = heapq.heappop(min_heap)
            head.next = l
            head = head.next

        return dummy.next

        
