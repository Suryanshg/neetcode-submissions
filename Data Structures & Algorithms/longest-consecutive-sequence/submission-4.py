class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        result = 0

        for n in nums:
            if n - 1 in num_set:
                continue

            end = n
            while end + 1 in num_set:
                end += 1

            result = max(result, end - n + 1)

        return result