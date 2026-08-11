class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count occurances of each task (alphabet)
        count_map = {}
        for t in tasks:
            if t in count_map:
                count_map[t] += 1
            else:
                count_map[t] = 1

        # Create a max heap using diff values of count map
        # We use the negative trick here to use min heap as max heap
        max_heap = [-c for c in count_map.values()]
        heapq.heapify(max_heap)

        # Starting cpu cycle at 0
        cpu_cycle = 0

        # Init an empty queue
        queue = []

        # While both max_heap and quque are not empty
        while max_heap or queue:

            # Increase the cpu cycle cunt
            cpu_cycle += 1

            # If Max Heap is not empty
            if max_heap:

                # Pop the top element and subtract 1 from it
                # This is similar to adding 1 to negative val of it
                # Which is already there in the heap
                c = 1 + heapq.heappop(max_heap)

                # If the value is not 0
                # Add it to the queue along with the cool down period
                # cool down period is current cpu_cycle + n
                if c:
                    queue.append([c, cpu_cycle + n])
            
            # If Queue is not empty and the first element's cool down is met
            # Pop it out from the queue and push it to the heap
            if queue and queue[0][1] == cpu_cycle:
                heapq.heappush(max_heap, queue.pop(0)[0])

        # return the cpu cycles
        return cpu_cycle
