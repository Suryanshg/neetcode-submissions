class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for ch in s1:
            s1_map[ch] = 1 + s1_map.get(ch, 0)
        
        # Sliding window of size len(s1) in s2
        window_size = len(s1)

        for l in range(0, len(s2) - window_size + 1):
            substr_map = {}
            substr = s2[l:l + window_size]
            for ch in substr:
                substr_map[ch] = 1 + substr_map.get(ch, 0)
            if substr_map == s1_map:
                return True
        return False
        