class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]
        current_max = 0
        for i in range(0, len(height) - 1):
            current_max = max(height[i], current_max)
            left_max.append(current_max)

        right_max = [0]
        current_max = 0
        for i in range(len(height) - 1, 0, -1):
            current_max = max(height[i], current_max)
            right_max.append(current_max)
        right_max = right_max[::-1]

        total_water_trapped = 0
        for i in range(len(height)):
            water_trapped = min(left_max[i], right_max[i]) - height[i]
            if water_trapped > 0:
                total_water_trapped += water_trapped

        return total_water_trapped


        