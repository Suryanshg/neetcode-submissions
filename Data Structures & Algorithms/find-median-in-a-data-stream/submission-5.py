class MedianFinder:

    def __init__(self):
        self.data = [] # Will always keep it sorted
        

    def addNum(self, num: int) -> None:
        l = 0
        r = len(self.data)
        while l < r:
            m = (l + r) // 2
            if num < self.data[m]:
                r = m
            else:
                l = m + 1

        self.data.insert(l, num)


    def findMedian(self) -> float:
        if len(self.data) % 2 != 0:
            return self.data[len(self.data) // 2]

        else:
            return (self.data[len(self.data) // 2] + self.data[(len(self.data) // 2) - 1]) / 2
        