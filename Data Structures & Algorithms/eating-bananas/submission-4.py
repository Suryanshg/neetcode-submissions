class Solution:
    def get_time(self, piles, k):
        time = 0
        for pile in piles:
            time += math.ceil(pile / k)
        return time 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = max(piles)
        while l < r:
            m = (l + r) // 2
            if self.get_time(piles, m) <= h:
                min_k = min(min_k, m)
                r = m
            else:
                l = m + 1
        return min_k


        
        