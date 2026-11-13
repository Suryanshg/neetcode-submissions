class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else: # min heap is at capacity
                n = heapq.heappop(min_heap)
                heapq.heappush(min_heap, max(n, num))
        return min_heap[0]