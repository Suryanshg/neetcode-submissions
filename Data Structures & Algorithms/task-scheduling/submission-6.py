class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = {}
        for task in tasks:
            task_counts[task] = task_counts.get(task, 0) + 1
        
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        q = deque()
        cycles= 0

        while max_heap or q:
            cycles += 1
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append((count, cycles + n))
            
            if q and q[0][1] == cycles:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return cycles