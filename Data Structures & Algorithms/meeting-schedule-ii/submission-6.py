"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # min meeting rooms == max number of meetings at any time
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        count = 0
        e = 0
        s = 0

        result = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            result = max(result, count)
        return result
        