class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map or len(self.time_map[key]) == 0:
            return ""
        values = self.time_map[key]
        
        # Binary Search
        l = 0
        r = len(values) - 1
        max_timestamp = values[r][1] 
        result = ""
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                max_timestamp = max(max_timestamp, values[m][1])
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result

        

        # [1, 2, 3, 6, 7]

        
