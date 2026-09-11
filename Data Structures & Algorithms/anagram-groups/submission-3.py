class Solution:
    def create_hash_tuple(self, s: str) -> Tuple[int]:
        """
        Takes in a string (s) and creates a tuple of 26 ints
        where each int tells the corresponding alphabet's 
        count in the string s. For example, count of number of 
        'a's in s would be at the tuple's 0 index.
        """
        hash_tuple = [0 for _ in range(26)]
        for ch in s:
            hash_tuple[ord(ch) - ord('a')] += 1
        return tuple(hash_tuple)



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        # For each string, create its hash tuple
        # And use it to create groups of anagrams
        for s in strs:
            hash_tuple = self.create_hash_tuple(s)
            if hash_tuple in groups:
                groups[hash_tuple].append(s)
            else:
                groups[hash_tuple] = [s]

        # Combine all anagram groups together into a list
        results = []
        for anagram_groups in groups.values():
            results.append(anagram_groups)

        # Return the list of anagrams
        return results