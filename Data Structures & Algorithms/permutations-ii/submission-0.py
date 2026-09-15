class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []

        # Construct a count map for each num in nums
        count_map = {n: 0 for n in nums}
        for n in nums:
            count_map[n] += 1


        def backtrack():
            # Base Case
            # Permutation is complete
            if len(perm) == len(nums):
                result.append(perm.copy())
                return

            
            for n in count_map:
                if count_map[n] > 0:
                    perm.append(n)
                    count_map[n] -= 1
                    backtrack()
                    count_map[n] += 1
                    perm.pop()
        
        backtrack()
        return result

        