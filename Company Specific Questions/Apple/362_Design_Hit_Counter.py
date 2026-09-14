"""
Problem Description
You need to design a hit counter system that tracks the number of hits received within the past 5 minutes (300 seconds).

The system should support two main operations:

1. Recording hits: When a hit occurs at a specific timestamp (in seconds), the system should record it. Multiple hits can happen at the same timestamp.
2.Querying hit count: Given a timestamp, the system should return the total number of hits that occurred in the past 300 seconds from that
timestamp. Specifically, it counts all hits in the time range [timestamp - 299, timestamp].

Key constraints and assumptions:

1. Timestamps are provided in seconds
2. Calls to the system happen in chronological order (timestamps are monotonically increasing)
3. Multiple hits may arrive at the same timestamp


The HitCounter class needs three methods:

1. HitCounter(): Initializes the hit counter system
2. hit(timestamp): Records a hit at the given timestamp
3. getHits(timestamp): Returns the count of all hits in the past 300 seconds from the given timestamp

For example, if hits occurred at timestamps 1, 2, 3, and 301, calling getHits(301) would return 1 (only the hit at timestamp 301 is within the 
past 300 seconds), while getHits(303) would still return 1 since the hit at timestamp 1 is now more than 300 seconds old.
"""
class HitCounter:
    def __init__(self):
        # We store all hits in a list
        self.hits = []


    def hit(self, timestamp: int) -> None:
        # We append all timestamps as it as the timestamps are monotonically increasing
        self.hits.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        # Since timestamps are monotonically increasing, we can do binary search for timestamp - 300 value

        # Init l and r and target timestamp
        l = 0
        r = len(self.hits)
        target = timestamp - 300

        # While l is less than or equal to r
        while l <= r:

            # Calculate the midpoint
            m = (l + r) // 2

            # if the value at m is less than the target
            # We search in the top half by setting l to m + 1
            if self.hits[m] <= target:
                l = m + 1

            # Otherwise the target value is in bottom half so we can move r to m - 1
            else:
                r = m - 1

        # Once we exit, we know we have the l value (index) which is the starting point of the 
        # sliding window of size 300 or less for calculating the number of hits
        # we can return len(hits) - l
        return len(self.hits) - l





# Driver code
if __name__ == '__main__':
    # Test 1
    hit_counter = HitCounter()
    hit_counter.hit(1)
    hit_counter.hit(2)
    hit_counter.hit(3)

    assert hit_counter.getHits(4) == 3

    hit_counter.hit(300)

    assert hit_counter.getHits(300) == 4
    assert hit_counter.getHits(301) == 3

    print("Test 1 Passed!")