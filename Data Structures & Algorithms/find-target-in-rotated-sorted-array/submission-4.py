class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            # if m is in left sorted portion
            if nums[l] <= nums[m]:

                # If target is greater than nums[m] or less than nums[l], we can search right
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                
                # Else search left
                else:
                    r = m - 1

            # if m is in right sorted portion
            else:

                # Search left if we are out of bounds in the right sorted portion
                if target < nums[m] or target > nums[r]:
                    r = m - 1

                # Else search right
                else:
                    l = m + 1


        return -1