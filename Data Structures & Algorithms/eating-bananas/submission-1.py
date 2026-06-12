class Solution:
    def calculate_hrs(self, piles: List[int], k):
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile / k)
        return hrs 



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find the max and min of the piles
        max_pile = 0
        for pile in piles:
            max_pile = max(max_pile, pile)

        l = 1
        r = max_pile
        min_k = max_pile
        while l <= r:
            k = (r + l) // 2
            hrs = self.calculate_hrs(piles, k)

            if hrs > h:
                l = k + 1
            else:
                min_k = min(k, min_k)
                r = k - 1

        return min_k