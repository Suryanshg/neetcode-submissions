class Solution:
    def get_anagram(self, word):
        anagram = [0 for _ in range(26)]
        for ch in word:
            anagram[ord(ch) - ord('a')] += 1
        return tuple(anagram)
            

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            anagram = self.get_anagram(word)      
            if anagram in anagram_map:
                anagram_map[anagram].append(word)
            else:
                anagram_map[anagram] = [word]

        grouped_anagrams = []
        for key in anagram_map:
            grouped_anagrams.append(anagram_map[key])

        return grouped_anagrams