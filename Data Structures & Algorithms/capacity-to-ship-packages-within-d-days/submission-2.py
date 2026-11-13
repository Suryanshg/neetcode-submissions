class Solution:
    def can_ship(self, weights, max_days, max_capacity):
        capacity = 0
        i = 0
        days = 0
        while i < len(weights):
            if capacity + weights[i] <= max_capacity:
                capacity += weights[i]
                i += 1
            else:
                capacity = 0
                days += 1

        if capacity:
            days += 1

        return days <= max_days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = (l + r) // 2
            if self.can_ship(weights, days, m):
                r = m
            else:
                l = m + 1
        return l