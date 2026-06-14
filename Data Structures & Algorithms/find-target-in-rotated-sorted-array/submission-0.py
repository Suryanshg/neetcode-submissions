class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            # Mid is in left sorted
            # Pivot idx lies in right part
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]: # Search right
                    l = m + 1
                else: # search left
                    r = m - 1

            
            # Mid is in right sorted
            # Pivot idx lies in left part
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1



        return -1