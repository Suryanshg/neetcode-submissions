class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_substr_len = 0
        l = 0
        for r in range(len(s)):
            # Update the frequency map
            freq_map[s[r]] = 1 + freq_map.get(s[r], 0)

            # If num of replacements needed exceeds what's allowed (k)
            # update the left pointer (shrink sliding window)
            # num replacements needed = len of substr - max freq in freq_map
            while (r - l + 1) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1


            # Calculate the max_substr_len
            # current substr len = r - l + 1
            max_substr_len = max(max_substr_len, r - l + 1)

        return max_substr_len
        