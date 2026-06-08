class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        # result = []
        monotonic_idx_stack = []
        i = 0
        while i < len(temperatures):
            print(monotonic_idx_stack)
            while monotonic_idx_stack and (temperatures[monotonic_idx_stack[-1]] < temperatures[i]):
                # print("pop")
                idx = monotonic_idx_stack.pop()
                result[idx] = i - idx
            monotonic_idx_stack.append(i)
            # print(result)
            i += 1
            # print("\n")

        # print(monotonic_idx_stack)
        # print(result)
        return result