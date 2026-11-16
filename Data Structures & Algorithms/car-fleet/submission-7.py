class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted([[p, s] for p, s in zip(position, speed)])
        
        stack = []

        # Because a faster car becomes slow when it catches up with the car ahead of it
        # Going in reverse direction based on positions allows to find and group faster and slower cars together
        for p, s in pairs[::-1]:
            t = (target - p) / s

            if not stack or stack[-1] < t:
                stack.append(t)
    
        return len(stack)
