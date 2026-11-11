class Solution:
    def can_ship(self, weights, max_days, max_capacity):
        days = 0
        current_capacity = 0

        i = 0
        while i < len(weights):
            if current_capacity + weights[i] <= max_capacity:
                current_capacity += weights[i]
                i += 1
            else:
                current_capacity = 0
                days += 1
        if current_capacity:
            days += 1

        return days <= max_days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        min_weight = sum(weights)
        while l < r:
            m = (l + r) // 2
            if self.can_ship(weights, days, m):
                r = m
                min_weight = min(min_weight, m)
            else:
                l = m + 1
        return min_weight
