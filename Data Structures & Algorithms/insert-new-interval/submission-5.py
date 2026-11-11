class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        # Find insert position in the intervals list
        i = 0
        while i < len(intervals): 
            if newInterval[0] < intervals[i][0]:
                break
            result.append(intervals[i])
            i += 1

        # Position i is the place where we can insert it
        # Merge it with last appended interval if necessary
        
        if result and result[-1][1] >= newInterval[0]:
            last_interval = result.pop()
            merged_interval = [last_interval[0], max(last_interval[1], newInterval[1])]
        else:
            merged_interval = newInterval


        for nxt in intervals[i:]:
            if merged_interval[1] >= nxt[0]:
                merged_interval[1] = max(merged_interval[1], nxt[1])
            else:
                result.append(merged_interval)
                merged_interval = nxt
        result.append(merged_interval)

        return result

        

        