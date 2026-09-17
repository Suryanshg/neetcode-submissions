class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by the start of interval
        intervals = sorted(intervals, key = lambda i: i[0])

        # Init merged intervals and current interval
        merged_intervals = []
        current_interval = intervals[0]

        # Go thru all intervals starting at idx 1
        for interval in intervals[1:]:

            # If current interval and iterator interval are overlapping
            # Merge iterator interval into current interval
            if interval[0] <= current_interval[1]:
                current_interval[0] = min(current_interval[0], interval[0])
                current_interval[1] = max(current_interval[1], interval[1])
            
            # Else, there is no overlap, so we append current interval to merged intervals
            # set interval to current_interval
            else:
                merged_intervals.append(current_interval)
                current_interval = interval

        # Add final current interval to merged intervals
        merged_intervals.append(current_interval)

        # Return merged intervals
        return merged_intervals
        