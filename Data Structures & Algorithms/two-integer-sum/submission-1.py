class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {} # Maps num -> idx in nums

        # For all different num in nums
        for i in range(len(nums)):

            # For this nums[i], calculate its nums[j] so that
            # nums[i] + nums[j] == target
            diff = target - nums[i]

            # If this nums[j] already in idx_map, return its index along with i in a list
            if diff in idx_map:
                return [idx_map[diff], i]

            # Otherwise add current num and its idx (i) to idx map
            idx_map[nums[i]] = i
        