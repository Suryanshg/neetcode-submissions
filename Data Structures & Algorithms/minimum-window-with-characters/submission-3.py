class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Make a count map for t
        t_count = {}
        for ch in t:
            t_count[ch] = 1 + t_count.get(ch, 0)

        # init variables for finding min_substr
        min_substr_len = float("infinity")
        min_substr = ""
        min_substr_map = {}
        
        # Sliding window: keep increasing window size and decrease it in case of a match (overlap)
        l = 0
        for r in range(len(s)):

            # Keep building min_substr_map
            min_substr_map[s[r]] = 1 + min_substr_map.get(s[r], 0)

            # check if t_count and min_substr_map has overlap
            overlap = True
            for ch in t_count.keys():
                if ch not in min_substr_map or t_count[ch] > min_substr_map[ch]:
                    overlap = False
                    break
            
            # while there is overlap
            while overlap:
                # Calculate and update min_substr
                if r - l + 1 < min_substr_len:
                    min_substr_len = len(s[l : r + 1])
                    min_substr = s[l : r + 1]

                # Keep moving left pointer to shrink window and update the map
                min_substr_map[s[l]] -= 1
                l += 1

                # check for overlap
                for ch in t_count.keys():
                    if ch not in min_substr_map or t_count[ch] > min_substr_map[ch]:
                        overlap = False
                        break                

        # Return the min_substr        
        return min_substr
        