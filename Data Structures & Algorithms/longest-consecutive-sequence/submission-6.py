class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0

        for num in num_set:
            if num - 1 in num_set:
                continue
            end = num + 1
            while end in num_set:
                end += 1
            result = max(result, end - num)
        
        return result