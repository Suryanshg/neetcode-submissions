class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [[-math.sqrt(p[0]**2 + p[1]**2) ,p[0], p[1]] for p in points]
        heapq.heapify(dists)
        print(dists)
        
        while len(dists) > k:
            heapq.heappop(dists)

        result = [[p[1], p[2]] for p in dists]


        return result
