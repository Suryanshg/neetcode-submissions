class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a max heap by using negating the stone values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # While the max heap has more than 1 element
        while len(max_heap) > 1:

            # Pop x and y (x >= y, confirmed)
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            # If x > y (strictly), then push -(x - y)
            if x > y:
                heapq.heappush(max_heap, -(x - y))

        return -max_heap[0] if max_heap else 0