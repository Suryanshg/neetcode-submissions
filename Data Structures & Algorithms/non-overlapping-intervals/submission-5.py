class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)

        end = intervals[0][1]
        count = 0

        for nxt in intervals[1:]:
            if end > nxt[0]:
                count += 1
                end = min(end, nxt[1])
            else:
                end = nxt[1]
        return count