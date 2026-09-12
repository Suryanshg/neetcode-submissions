class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        longest_len = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                longest_len = max(longest_len, r - l + 1)
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                # seen.add(s[r])

        return longest_len
        