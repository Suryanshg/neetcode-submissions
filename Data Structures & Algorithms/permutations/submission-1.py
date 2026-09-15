class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time: n! * n^2
        # Space: n! * n

        # If nums is empty, return empty List of Lists
        if len(nums) == 0:
            return [[]]

        # Sub problem: Get permutations of subarray without first element
        perms = self.permute(nums[1:])

        # Init list to store all perms
        result = []

        # Then insert the first element at every position 1 by 1
        # for each permutation of the subarray
        for perm in perms:
            for i in range(len(perm) + 1): # For all possible positions
                # make a fresh copy of the current permutation
                perm_copy = perm.copy()

                # Add the first element at current chosen position
                perm_copy.insert(i, nums[0])

                # Add the new permutation to the result array
                result.append(perm_copy)

        # Return the result
        return result


        