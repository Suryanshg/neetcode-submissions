class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # Stores (start_idx, height)
        for i, h in enumerate(heights):
            # Starting at i, can be extended towards left 
            start_idx = i 
            while stack and stack[-1][1] > h:
                idx, height = stack.pop() # Pop the top
                
                # Calculate max area
                # Area is height * width (current index (i) - popped element's start_idx (left boundary))
                max_area = max(max_area, height * (i - idx))

                # Update current start_idx to be popped element's start_idx
                # as h < popped element's height (so its left boundary extends) 
                start_idx = idx 
            stack.append((start_idx, h))
        
        # Calculate area for remaining elements in the stack
        # We will use start_idx as left boundary and len(heights) as right boundary
        # len(heights) as right boundary since these elements stayed in the stack
        # Thus, can be extended towards the end
        for start_idx, height in stack:
            max_area = max(max_area, height * (len(heights) - start_idx))

        return max_area
            