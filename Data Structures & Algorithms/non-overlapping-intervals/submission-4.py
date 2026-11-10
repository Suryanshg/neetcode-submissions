class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)

        end = intervals[0][1]
        erasals = 0
        for nxt in intervals[1:]:
            if end > nxt[0]: # There is overlap
                erasals +=1
                end = min(end, nxt[1])
            else: # No overlap
                end = nxt[1]

        return erasals