class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for c in range(len(nums) - 2):
            l = c + 1
            r = len(nums) - 1
            
            while l < r:
                if nums[l] + nums[r] + nums[c] == 0:
                    triplets.add(tuple([nums[c], nums[l], nums[r]]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + nums[c] < 0:
                    l += 1
                else:
                    r -= 1
        return list(triplets)