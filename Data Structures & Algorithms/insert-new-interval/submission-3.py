class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        idx = None
        # Find the location to insert
        for i, interval in enumerate(intervals):
            if newInterval[0] < interval[0]:
                idx = i
                break
            result.append(interval)

        # Merge with preceding interval if needed
        if result and result[-1][1] >= newInterval[0]:
            result[-1][1] = max(result[-1][1], newInterval[1])
        else:
            result.append(newInterval)

        

        # Add remaining elements and merge (if necessary)
        if idx is not None:
            prev_interval = result.pop()
            for j in range(idx, len(intervals)):
                if prev_interval[1] >= intervals[j][0]:
                    prev_interval[1] = max(prev_interval[1], intervals[j][1])
                else:
                    result.append(prev_interval)
                    prev_interval = intervals[j]
            
            result.append(prev_interval)

        return result

        


