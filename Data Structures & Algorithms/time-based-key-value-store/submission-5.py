class TimeMap:

    def __init__(self):
        self.data = {} # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.data:
            return result

        values = self.data[key]
        l = 0
        r = len(values) - 1
        # print(values)
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                l = m + 1
                result = values[m][1]
            else:
                r = m - 1
        return result
