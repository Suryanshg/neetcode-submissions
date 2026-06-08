class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        monotonic_idx_stack = []
        i = 0
        while i < len(temperatures):
            while monotonic_idx_stack and (temperatures[monotonic_idx_stack[-1]] < temperatures[i]):
                idx = monotonic_idx_stack.pop()
                result[idx] = i - idx
            monotonic_idx_stack.append(i)
            i += 1
        return result