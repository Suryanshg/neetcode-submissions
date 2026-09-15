class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = [] # Maintain all permutations found
        perm = [] # Maintain the current permutation being constructed

        # Construct a count map for each num in nums
        count_map = {n: 0 for n in nums}
        for n in nums:
            count_map[n] += 1

        # Backtracking DFS Helper
        def dfs():
            # Base Case
            # Permutation is complete
            # We append the permutation's copy into the result
            # and exit the recursion
            if len(perm) == len(nums):
                result.append(perm.copy())
                return

            # For every unique element in count map
            for n in count_map:

                # If the count of element is greater than 0
                if count_map[n] > 0:

                    # We explore adding it to the permutation
                    perm.append(n)      # Add to permutation
                    count_map[n] -= 1   # Decrease its count
                    dfs()               # DFS remaining elements
                    count_map[n] += 1   # Now explored, Increase its count
                    perm.pop()          # Remove from permutation
        
        # Perform DFS with empty permutation
        dfs()

        # Return the result array
        return result

        