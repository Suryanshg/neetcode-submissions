class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in idx_map:
                return [idx_map[diff], i]
            idx_map[nums[i]] = i
        