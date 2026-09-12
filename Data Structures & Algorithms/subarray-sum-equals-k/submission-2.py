class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        # Keep track of current sum
        current_sum = 0

        # Keep track of prefix sums encountered
        # Starting with empty subarray sum = 0 with a count of 1
        prefix_sums = {0: 1}

        # For each n in nums
        for n in nums:

            # Accumulate current sum
            current_sum += n

            # Calc diff
            diff = current_sum - k

            # Increment count if the diff had an count entry in prefix sums map
            count += prefix_sums.get(diff, 0)

            # Update current sum's count in prefix sum or add it if it does not exist
            prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)

        # return the count
        return count