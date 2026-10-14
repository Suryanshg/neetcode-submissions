class MedianFinder:

    def __init__(self):
        self.first = [] # will be a max heap
        self.second = [] # will be a min heap
        

    def addNum(self, num: int) -> None:
        # Add num to first half
        heapq.heappush(self.first, -num) 

        # Move max of first half up so every element in half is <= every element in second
        heapq.heappush(self.second, -heapq.heappop(self.first))

        # Rebalance to make sure first half always have 1 extra than second half
        if len(self.second) > len(self.first):
            heapq.heappush(self.first, -heapq.heappop(self.second))

    def findMedian(self) -> float:
        if len(self.first) > len(self.second):
            return -self.first[0]
        return (-self.first[0] + self.second[0]) / 2
        