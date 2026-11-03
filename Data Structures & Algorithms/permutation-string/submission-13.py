class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_counts = Counter(s1)
        s2_counts = Counter(s2[:len(s1)])
        if s1_counts == s2_counts:
            return True

        for r in range(len(s1), len(s2)):
            s2_counts[s2[r]] += 1
            s2_counts[s2[r - len(s1)]] -= 1
            if s2_counts == s1_counts:
                return True

        return False