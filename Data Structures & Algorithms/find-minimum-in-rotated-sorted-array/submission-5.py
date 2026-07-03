class Solution:
    def findMin(self, nums: List[int]) -> int:
        # IDEA: Use Binary search to find the sorted sub array and return the min (l) of that
        l, r = 0, len(nums) -1 
        min_nums = nums[l]

        while l <= r:

            # If we get to a subportion thats already sorted
            if nums[l] < nums[r]:
                min_nums = min(min_nums, nums[l])
                break

            m = (r + l) // 2
            min_nums = min(min_nums, nums[m])

            # If m in left sorted portion
            if nums[m] >= nums[l]:
                l = m + 1 # search right


            # If m in right sorted portion
            else:
                r = m - 1 # search left
            
        # return min_nums
        return min_nums
        
        