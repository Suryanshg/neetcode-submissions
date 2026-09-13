"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # Get sorted start and end times
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])

        # Init variables for counting num of meeting rooms needed at each point of time
        result, count = 0, 0
        s, e = 0, 0

        # While we have not exhausted any start times
        while s < len(intervals):

            # If current start time is less than the next ending time
            # Increase the count by 1
            # move to the next start time
            if start_times[s] < end_times[e]:
                count += 1
                s += 1

            # Otherwise, decrease count by 1 (as a meeting has ended and we move to a new meeting)
            # and move to the next end time
            else:
                count -= 1
                e += 1

            # update the result using max of prev result and count
            result = max(result, count)

        # Return the result
        return result 
        