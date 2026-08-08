class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Create a new list of lists where at 0 idx we have dist from origin
        # and at idx 1 and 2 we have x and y coords
        # Keeping dists as negative to implement a max heap
        dists = [[-math.sqrt(p[0]**2 + p[1]**2) ,p[0], p[1]] for p in points]
        heapq.heapify(dists)
        
        # While there are greater than k elements in the max heap, keep popping
        while len(dists) > k:
            heapq.heappop(dists)

        # Compine the results of remaining k values into a result array to preserve only
        # x and  y coords
        result = [[p[1], p[2]] for p in dists]

        # return the result array
        return result
