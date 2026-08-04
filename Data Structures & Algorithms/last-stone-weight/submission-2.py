class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a max heap by using negating the stone values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x != y:
                heapq.heappush(max_heap, -abs(y - x))

        return -max_heap[0] if max_heap else 0