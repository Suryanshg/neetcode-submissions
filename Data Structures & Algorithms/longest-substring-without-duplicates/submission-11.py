class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        r = 0
        idx_map = {}
        while r < len(s):
            if s[r] in idx_map and idx_map[s[r]] >= l:
                l = idx_map[s[r]] + 1
            idx_map[s[r]] = r
            r += 1
            result = max(result, r - l)
            # print(r, l)
        return result
        