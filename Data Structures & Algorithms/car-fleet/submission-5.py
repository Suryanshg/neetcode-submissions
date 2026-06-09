class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Init time stack
        # It will have a strict monotonically increasing property
        time_stack = []

        # Get sorted indices for positions (Descending)
        # Faster cars (less time) behind a slower car (more time) will have to join the slower car as a fleet
        sorted_indices = sorted(range(len(position)), key=lambda i: position[i], reverse=True)

        # For all sorted indices in descending order
        for i in sorted_indices:
            # calculate time of the current car at position[i]
            time = (target - position[i]) / speed[i]

            # If time is greater than the top of the stack
            # Means it must be a new fleet
            if not time_stack or time > time_stack[-1]:
                time_stack.append(time)

        # Len of stack is the number of fleets
        return len(time_stack)