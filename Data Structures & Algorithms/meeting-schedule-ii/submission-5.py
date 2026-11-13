"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Min number of rooms is max number of meetings happening at any point of time
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        s = 0
        e = 0
        count = 0
        result = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            result = max(count, result)

        return result
