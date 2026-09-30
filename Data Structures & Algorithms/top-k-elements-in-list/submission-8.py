class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency map for each number
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # Store each num, freq in max heap
        # Negate the freq to make it max heap
        max_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(max_heap, (-freq, num))
        
        # Maintain a list of top k elements by frequency
        # At every iter, we pop from max_heap and store the num in top_k
        top_k = []
        while len(top_k) != k:
            _, num = heapq.heappop(max_heap)
            top_k.append(num)
        
        # Return top_k
        return top_k
        
