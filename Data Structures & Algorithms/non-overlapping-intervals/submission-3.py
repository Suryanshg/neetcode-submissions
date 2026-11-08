class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals) # Primary sort by start, secondary sort by end

        result = 0
        end = intervals[0][1]

        for nxt in intervals[1:]:
            if end > nxt[0]:
                result += 1
                end = min(end, nxt[1]) # an interval with smaller end can only conflict with fewer later intervals, never more.
            else:
                end = nxt[1]
        
        return result
        