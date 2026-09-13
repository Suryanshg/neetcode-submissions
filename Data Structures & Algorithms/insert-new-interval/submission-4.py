class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        # Find the location to insert
        idx = 0
        for interval in intervals:
            if newInterval[0] < interval[0]:
                break
            result.append(interval)
            idx+=1

        # Merge with preceding interval if there is any and if needed
        if result and result[-1][1] >= newInterval[0]:
            result[-1][1] = max(result[-1][1], newInterval[1])
        else: # if no merge is required, add the new interval to the result list
            result.append(newInterval)

        

        # Add remaining elements and merge (if necessary)
        prev_interval = result.pop()
        for j in range(idx, len(intervals)):

            # If prev interval is overlapping with the current one
            # Merge current into prev interval
            if prev_interval[1] >= intervals[j][0]:
                prev_interval[1] = max(prev_interval[1], intervals[j][1])

            # Otherwise add previous interval to the result and
            # set current interval as the previous one
            else:
                result.append(prev_interval)
                prev_interval = intervals[j]
        
        # Add the remaining interval
        result.append(prev_interval)

        # Return the result
        return result

        


