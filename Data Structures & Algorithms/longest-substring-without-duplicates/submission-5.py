class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Init left and right pointers of the window
        l, r = 0, 0

        # Maintain a set of seen characters
        seen = set()

        longest_len = 0

        # While r is less than len of s
        while r < len(s):

            # If char at r is not seen yet
            # We add it to seen set
            # Recalculate longest len using size of current window
            # Increment r
            if s[r] not in seen:
                seen.add(s[r])
                longest_len = max(longest_len, r - l + 1)
                r += 1

            # Otherwise, char at r is a repeated char
            # So while it is existing in seen
            # We reduce the sliding window by incrementing l
            # and also removing char at l from seen set
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

        # Return the longest len so far
        return longest_len
        