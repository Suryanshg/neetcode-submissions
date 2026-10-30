class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        r = 0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
    
            seen.add(s[r])
            r += 1
            
            result = max(result, r - l)
        return result
        