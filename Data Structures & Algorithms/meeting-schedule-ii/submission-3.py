"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append((interval.start, "s"))
            times.append((interval.end, "e"))
        times = sorted(times) # Primary sort on timestamps, secondary on start vs end where end is winner
        count = 0
        result = 0
        for time in times:
            if time[1] == "s":
                count += 1
            else:
                count -= 1
            result = max(result, count)
        return result
    
        