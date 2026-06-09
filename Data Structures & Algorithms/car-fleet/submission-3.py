class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_stack = []
        sorted_indices = sorted(range(len(position)), key=lambda i: position[i], reverse=True)
        for i in sorted_indices:
            time = (target - position[i]) / speed[i]
            if not time_stack or time > time_stack[-1]:
                time_stack.append(time)
            i += 1
        return len(time_stack)