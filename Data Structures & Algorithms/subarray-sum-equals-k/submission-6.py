class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums = sorted(nums)
        prefix_sum_map = {0 : 1}
        current_sum = 0
        total = 0

        for n in nums:
            current_sum += n
            total += prefix_sum_map.get(current_sum - k, 0)
            prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1

        return total
        