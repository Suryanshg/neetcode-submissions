class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the numbers so they are in increasing order
        nums.sort()

        # Maintain a set of tuples
        triplets = set()

        # For all num in nums except for last two ones
        for c in range(len(nums) - 2):

            # We start two pointers l and r, l begins just after c, r begins from the end of list
            l = c + 1
            r = len(nums) - 1

            # While l is less than r and until they are exactly beside each other
            while l < r:

                # We check if nums at l, r and c sum to 0
                # If they do, we move pointers closer and record c, l, and r inside triplets as a tuple
                if nums[l] + nums[r] + nums[c] == 0:
                    triplets.add(tuple([nums[c], nums[l], nums[r]]))
                    l += 1
                    r -= 1

                # If the value is less than 0, that means we need to increase l
                elif nums[l] + nums[r] + nums[c] < 0:
                    l += 1

                # Else, value is greater than 0, so we decrease r
                else:
                    r -= 1

        # Convert the set of triplets to a list and return
        return list(triplets)