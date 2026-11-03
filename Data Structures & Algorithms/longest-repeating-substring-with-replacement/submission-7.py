class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        result = 0
        l = 0
        for r in range(len(s)):

            # Increment Freq of current char
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1


            # If # of replacements needed exceed k, then move l ptr forward
            while (r - l + 1) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1

            # Now we have a substring with valid # of replacements
            # Hence, we can check and update the result
            result = max(result, r - l + 1)


        return result

