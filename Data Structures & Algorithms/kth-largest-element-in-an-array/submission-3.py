class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(max_heap, (-num, i))
        
        while k and max_heap:
            x, _ = heapq.heappop(max_heap)
            k -= 1
        
        return -x
