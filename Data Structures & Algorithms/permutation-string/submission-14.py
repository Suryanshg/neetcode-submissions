class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_counts = {}
        s2_counts = {}

        for i, ch in enumerate(s1):
            s1_counts[ch] = s1_counts.get(ch, 0) + 1
            s2_counts[s2[i]] = s2_counts.get(s2[i], 0) + 1

        if s1_counts == s2_counts:
            return True

        for i in range(len(s1), len(s2)):
            # Account for new char
            s2_counts[s2[i]] = s2_counts.get(s2[i], 0) + 1

            # Account for prev (leftmost) char
            s2_counts[s2[i - len(s1)]] -= 1
            if s2_counts[s2[i - len(s1)]] == 0:
                del s2_counts[s2[i - len(s1)]]

            if s1_counts == s2_counts:
                return True

        return False