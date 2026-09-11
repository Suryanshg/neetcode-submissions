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
        # For each idx in freq_buckets where idx is frequency, we store a list of
        # elements of nums which have that frequency
        freq_buckets = [[] for _ in range(len(nums) + 1)] 

        # Now we populate the buckets
        for num in freq_map.keys():
            # Get frequency of num
            freq = freq_map[num]

            # Add num to a bucket based on its freq
            freq_buckets[freq].append(num)

        # Now we find the top k frequent elements
        top_k = []
        for bucket in freq_buckets[::-1]: # Going in reverse order
            # If we found top k, we can break out
            if len(top_k) >= k:
                break

            top_k.extend(bucket)
        
        # Return the top k results
        return top_k
        
