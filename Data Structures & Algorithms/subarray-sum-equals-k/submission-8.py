class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0 : 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum  += num
            count += prefix_sum.get(current_sum - k, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return count
        