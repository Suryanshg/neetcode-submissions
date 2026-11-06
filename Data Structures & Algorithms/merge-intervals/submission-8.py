class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals) # Sort by start timestamp
        merged_intervals = []
        current = intervals[0]
        for nxt in intervals[1:]:
            if current[1] >= nxt[0]:
                current[1] = max(nxt[1], current[1])
            else:
                merged_intervals.append(current)
                current = nxt

        merged_intervals.append(current)

        return merged_intervals
        