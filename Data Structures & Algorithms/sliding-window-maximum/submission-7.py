class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        idx_deque = deque()
        maxes = []
        l = r = 0
        while r < len(nums):
            # Remove indices whose values are smaller than nums[r]
            while idx_deque and nums[idx_deque[-1]] < nums[r]:
                idx_deque.pop()
            idx_deque.append(r)

            # If left ptr passes front idx, remove it
            if l > idx_deque[0]:
                idx_deque.popleft()
            
            # If deque is full, use first element as max
            if (r + 1) >= k:
                maxes.append(nums[idx_deque[0]])
                l += 1 # move l ptr

            # Expand the window
            r += 1

        return maxes