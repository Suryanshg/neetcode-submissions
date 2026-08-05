class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a max heap using negate technique
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        
        # Keep removing from the top (max element) k - 1 times
        i = 1
        while i < k:
            heapq.heappop(max_heap)
            i += 1
    
        # The item now at the top will be kth largest, so unnegate that and return
        return -max_heap[0]