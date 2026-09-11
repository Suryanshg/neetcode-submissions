class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency map for each number
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # each num in nums can have frequency in range 0 - len(nums)
        # We need len(nums) + 1 buckets of frequencies and in each bucket
        # we keep what all elements of nums fall into
        # For each idx in freq_buckets where idx is frequency, we store a set of
        # elements of nums which have that frequency
        freq_buckets = [set() for _ in range(len(nums) + 1)] 

        # Now we populate the buckets
        for num in nums:
            # Get frequency of num
            freq = freq_map[num]

            # Add num to a bucket based on its freq
            freq_buckets[freq].add(num)

        # Now we find the top k frequent elements
        top_k = []
        for bucket in freq_buckets[::-1]:
            if len(top_k) >= k:
                break
            for item in bucket:
                top_k.append(item)
        
        return top_k
        
