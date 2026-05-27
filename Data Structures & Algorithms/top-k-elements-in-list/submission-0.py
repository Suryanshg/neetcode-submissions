class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        freq_buckets = [[] for _ in range(len(nums) + 1)]

        for num in freq_map.keys():
            freq = freq_map[num]
            freq_buckets[freq].append(num)

        top_k_frequent = []
        for bucket in freq_buckets[::-1]:
            if len(bucket) > 0:
                top_k_frequent.extend(bucket)
                if len(top_k_frequent) == k:
                    break


        return top_k_frequent

        