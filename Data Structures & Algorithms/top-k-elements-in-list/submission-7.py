class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency map for each number
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        max_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(max_heap, (-freq, num))
        
        top_k = []
        while len(top_k) != k:
            _, num = heapq.heappop(max_heap)
            top_k.append(num)
        
        return top_k
        
