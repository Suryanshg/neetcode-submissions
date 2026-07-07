# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Init ptrs for both lists
        l1 = list1
        l2 = list2

        # Init a new node, which will be a dummy node and start a head ptr 
        node = ListNode()
        head = node

        # While there are still elements in l1 and l2
        while l1 and l2:

            # If l1's val is less than l2
            # Point head's next to l1
            # move l1 forward
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next

            # Else point head's next to l2
            # move l2 forward
            else:
                head.next = l2
                l2 = l2.next
   
            # Move head forward
            head = head.next

        # point remainder of l1 or l2 to head's next
        head.next = l1 or l2
        
        # Return dummy node's next
        return node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If lists is empty, return None
        if len(lists) == 0:
            return None

        # Init first list as the merged list
        merged_list = lists[0]

        # for all other unmerged lists
        for unmerged_list in lists[1:]:

            # Merge them into merged list using the mergeTwoLists algo
            merged_list = self.mergeTwoLists(merged_list, unmerged_list)

        # Return the merged list
        return merged_list

        