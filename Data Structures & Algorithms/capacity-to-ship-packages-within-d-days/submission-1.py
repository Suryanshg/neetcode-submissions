class Solution:
    def can_ship(self, weights, max_days, max_capacity):
        days = 0
        i = 0
        current_capacity = 0
        while i < len(weights):
            if current_capacity + weights[i] <= max_capacity:
                current_capacity += weights[i]
                i += 1
            else:
                days += 1
                current_capacity = 0
        if current_capacity:
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
