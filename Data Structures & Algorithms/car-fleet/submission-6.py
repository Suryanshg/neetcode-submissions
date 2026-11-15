class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted([[p, s] for p, s in zip(position, speed)])

        stack = []

        for p, s in pairs[::-1]:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)