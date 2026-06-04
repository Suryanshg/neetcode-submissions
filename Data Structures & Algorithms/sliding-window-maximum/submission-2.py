class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr_max = max(nums[0:k])
        result = [arr_max]
        l = 1
        for r in range(k, len(nums)):
            arr_max = max(nums[l:r + 1])
            result.append(arr_max)
            l += 1
        return result