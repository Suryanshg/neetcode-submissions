class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        explored = set()

        result = 0
        for num in nums:
            if num in explored:
                continue

            start = num
            while start in nums_set:
                explored.add(start)
                start -= 1
            result = max(result, num - start)
        
        return result
            