class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_map = {}
        max_len = 0
        start = 0
        ptr = 0
        while ptr < len(s):
            if s[ptr] in seen_map:
                start = seen_map[s[ptr]] + 1
                max_len = max(max_len, ptr - start)
                ptr = start
                seen_map.clear()
            else:
                seen_map[s[ptr]] = ptr
                ptr += 1
                max_len = max(max_len, ptr - start)

        return max_len