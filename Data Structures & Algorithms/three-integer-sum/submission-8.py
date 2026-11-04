class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        seen = set()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                # print(nums[i], nums[j], nums[k])
                if nums[i] + nums[j] + nums[k] == 0:
                    if (nums[i], nums[j], nums[k]) not in seen:
                        result.append([nums[i], nums[j], nums[k]])
                        seen.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return result
        