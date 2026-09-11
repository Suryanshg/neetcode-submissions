class Solution:
    def create_hash_list(self, s: str) -> Tuple[int]:
        """
        Takes in a string (s) and creates a tuple of 26 ints
        where each int tells the corresponding alphabet's 
        count in the string s. For example, count of number of 
        'a's in s would be at the list's 0 index.
        """
        hash_list = [0 for _ in range(26)]
        for ch in s:
            hash_list[ord(ch) - ord('a')] += 1
        return tuple(hash_list)



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        # For each string, create its hash list
        # And use it to create groups of anagrams
        for s in strs:
            hash_list = self.create_hash_list(s)
            if hash_list in groups:
                groups[hash_list].append(s)
            else:
                groups[hash_list] = [s]

        results = []
        for group in groups.keys():
            results.append(groups[group])

        return results