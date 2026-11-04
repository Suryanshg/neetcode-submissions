class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_map = {0 : 1}

        for num in nums:
            current_sum += num
            count += prefix_map.get(current_sum - k, 0)
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

        return count
        