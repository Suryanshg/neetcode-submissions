# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If there are no lists, return None
        if len(lists) == 0:
            return None

        # Init a min heap by storing all values in it
        min_heap = []

        # For each list, we add all its values to the min heap
        # We add (list_node.value, i, list_node)
        # Here i works as a tie breaker
        i = 0
        for l in lists:
            while l:
                heapq.heappush(min_heap, (l.val, i, l))
                l = l.next
                i+=1 
        
        # Create a dummy node and init a head ptr
        dummy = ListNode(0)
        head = dummy

        # While there are still elements in the min heap
        while min_heap:

            # Pop out the elements based on the min value
            _, _, l = heapq.heappop(min_heap)

            # Set the head's next to point to the min value node
            head.next = l

            # Move the head to its next
            head = head.next

        # Return the dummy node's next, as it will be beginning of this linked list
        return dummy.next

        
