class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        # Sub problem: Get permutations of subarray without first element
        perms = self.permute(nums[1:])

        result = []

        # Then insert the first element at every position 1 by 1
        # for each permutation of the subarray
        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                result.append(perm_copy)

        return result


        