"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        ints = sorted([[i.start, i.end] for i in intervals])

        cur = ints[0]

        for nxt in ints[1:]:
            if cur[1] > nxt[0]:
                return False
            cur = nxt


        return True

        