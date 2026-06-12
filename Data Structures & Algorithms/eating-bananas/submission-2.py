class Solution:
    def calculate_hrs(self, piles: List[int], k):
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile / k)
        return hrs 



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find the max of the piles
        # This will allow us to determine the max value of k
        # as eating at a rate of max(piles) will result in 
        # len(piles) hrs.
        max_pile = 0
        for pile in piles:
            max_pile = max(max_pile, pile)

        # Set min bound of k as 1
        # Set max bound of k as max(piles)
        # Start with min_k as max(piles)
        l = 1
        r = max_pile
        min_k = max_pile

        # While l is less than or equal to r
        while l <= r:

            # Calculate k at min point of r and l
            k = (r + l) // 2

            # Calculate hours taken at k rate
            hrs = self.calculate_hrs(piles, k)

            # if hrs exceeds allowed h, then increase eating rate
            # That means increasing the lower bound
            if hrs > h:
                l = k + 1

            # Else hrs less than or equals h
            # Recalculate min_k
            # We can now decrease k by decreasing the upper bound
            else:
                min_k = min(k, min_k)
                r = k - 1

        # return min_k
        return min_k