class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_consecutive_count = 0
        for num in num_set:
            consecutive_count = 0
            while num + consecutive_count in num_set:
                consecutive_count += 1
            max_consecutive_count = max(max_consecutive_count, consecutive_count)

        return max_consecutive_count
        