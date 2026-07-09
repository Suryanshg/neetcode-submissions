# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def getKth(self, curr, k):
        i = 0
        while curr and i < k:
            curr = curr.next
            i += 1
        return curr 

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # prevGroup denotes last element of previous Group
        prevGroup = dummy

        while True:
            # Get kth node
            kth = self.getKth(prevGroup, k)

            # If its None, break out
            if kth is None:
                break

            # Set the nextGroup to be kth.next, as kth is last node of currentGroup
            nextGroup = kth.next

            # Reverse logic
            # Start with prev and curr
            # prev is kth.next as we want the currentGroup head to point to nextGroup's head
            # (Since currentGroup will be reversed)
            prev, curr = kth.next, prevGroup.next

            # Reverse until we reach the nextGroup
            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Save the prevGroup's next
            nxt = prevGroup.next

            # point prevGroup to the kth node (which becomes the first node of currentGroup after reversal)
            prevGroup.next = kth

            # Move prevGroup to its old next (which will be the last node of currentGroup)
            prevGroup = nxt


        return dummy.next