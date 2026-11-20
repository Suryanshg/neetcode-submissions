class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                x = heapq.heappop(heap)
                heapq.heappush(heap, max(x, num))
        
        return heap[0]