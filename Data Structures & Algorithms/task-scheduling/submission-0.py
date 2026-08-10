class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = {}
        for t in tasks:
            if t in count_map:
                count_map[t] += 1
            else:
                count_map[t] = 1

        max_heap = [-c for c in count_map.values()]
        heapq.heapify(max_heap)

        print(max_heap)
        t = 0
        queue = []

        while max_heap or queue:
            t += 1

            if max_heap:
                c = 1 + heapq.heappop(max_heap)

                if c:
                    queue.append([c, t + n])
            
            if queue and queue[0][1] == t:
                heapq.heappush(max_heap, queue.pop(0)[0])
            # print(queue)
            # break
        return t
