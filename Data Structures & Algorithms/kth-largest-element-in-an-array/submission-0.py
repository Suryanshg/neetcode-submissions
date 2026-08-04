class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        
        i = 1
        while i < k:
            heapq.heappop(max_heap)
            i += 1
    
        return -max_heap[0]