class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 is smaller than s1, return False immediately
        if len(s2) < len(s1):
            return False

        # Construct count map for s1 and s2(upto same len as s1's len)
        s1_map = {}
        s2_map = {}
        for i in range(len(s1)):
            s1_map[s1[i]] = 1 + s1_map.get(s1[i], 0)
            s2_map[s2[i]] = 1 + s2_map.get(s2[i], 0)

        # Compare the maps and if they are equal, return True
        if s1_map == s2_map:
            return True

        # Sliding Window
        l = 0

        # For all the remaining right pointer values
        for r in range(len(s1), len(s2)):

            # Move l up and update the count map
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]
            l += 1

            # Update count map with the new r
            s2_map[s2[r]] = 1 + s2_map.get(s2[r], 0)
            
            # check again
            if s1_map == s2_map:
                return True

        
        # return False at the end
        return False
        