class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        r = 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                result = max(result, r - l)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            result = max(result, r - l)
        return result
        