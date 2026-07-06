class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # While left is less than or equal to r
        while l <= r:

            # Calculate mid
            m = (l + r) // 2
            
            # If target is at mid location, return mid
            if target == nums[m]:
                return m

            # If Mid is in left sorted then
            # Pivot idx lies in right part
            if nums[m] >= nums[l]:

                # If target is greater than nums[m] or target is less than current left
                # Then we should search in the right part
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: # search left
                    r = m - 1

            
            # If Mid is in right sorted then
            # Pivot idx lies in left part
            else:
                # If the target is lesser than nums[m] or is greater than current right
                # Then we search in the left part
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else: # search right
                    l = m + 1

        # Return -1 as default
        return -1