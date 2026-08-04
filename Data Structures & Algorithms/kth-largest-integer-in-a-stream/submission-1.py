class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Store as member variables
        self.k = k
        self.min_heap = nums
        
        # Create a heap from min_heap (nums)
        heapq.heapify(self.min_heap)

        # Keep popping from the top until len of min_heap == k
        # This allows to find the k'th largest element to be at 
        # the top of the heap
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add the val to min_heap
        heapq.heappush(self.min_heap, val)

        # If length of min_heap exceeds k, pop out the min val
        # The next min will be the kth largest
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # Return the top of the heap (kth largest)
        return self.min_heap[0]