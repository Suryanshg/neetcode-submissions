class MedianFinder:

    def __init__(self):
        self.first = [] # will be a max heap
        self.second = [] # will be a min heap
        

    def addNum(self, num: int) -> None:
        # by default add value to first half
        heapq.heappush(self.first, -num)

        # Check if max of first half is less than min of second half
        if self.first and self.second and -self.first[0] > self.second[0]:
            val = -heapq.heappop(self.first)
            heapq.heappush(self.second, val)

        # Rebalancing
        # Check if diff of len between first and second does not exceed 1
        if len(self.first) > len(self.second) + 1:
            val = -heapq.heappop(self.first)
            heapq.heappush(self.second, val)

        if len(self.second) > len(self.first) + 1:
            val = heapq.heappop(self.second)
            heapq.heappush(self.first, -val)

    def findMedian(self) -> float:
        if len(self.first) > len(self.second):
            return -self.first[0]

        elif len(self.second) > len(self.first):
            return self.second[0]

        else:
            return (-self.first[0] + self.second[0]) / 2        