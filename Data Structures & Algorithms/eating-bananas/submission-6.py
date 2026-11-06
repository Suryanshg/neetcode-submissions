class Solution:
    def get_time(self, piles, k):
        time = 0
        for pile in piles:
            time += (pile + k - 1) // k
        return time 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            if self.get_time(piles, m) <= h:
                r = m
            else:
                l = m + 1
        return l


        
        