class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Init result array as 0 for all indices and monotonic idx stack
        result = [0 for _ in range(len(temperatures))]
        monotonic_idx_stack = []

        # iterate thru all temperatures
        i = 0
        while i < len(temperatures):

            # While current head of stack has a temperature less than current temperate
            # Keep popping out the head and updating the result list using different between idx (popped) and i
            while monotonic_idx_stack and (temperatures[monotonic_idx_stack[-1]] < temperatures[i]):
                idx = monotonic_idx_stack.pop()
                result[idx] = i - idx

            # Add the current i to the stack
            monotonic_idx_stack.append(i)
            i += 1

        # return the result
        return result