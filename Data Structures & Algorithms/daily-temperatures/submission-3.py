class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]
        idx_stack = []
        i = 0
        while i < len(temperatures):

            while idx_stack and temperatures[i] > temperatures[idx_stack[-1]]:
                idx = idx_stack.pop()
                result[idx] = i - idx

            idx_stack.append(i)
            i += 1

        return result