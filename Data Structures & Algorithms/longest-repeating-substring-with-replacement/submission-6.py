class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        l = 0
        r = 0
        result = 0
        while r < len(s):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1

            while (r - l + 1) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

            r+= 1

        return result
        