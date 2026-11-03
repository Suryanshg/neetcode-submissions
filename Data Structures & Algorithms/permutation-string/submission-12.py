class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_map = {}
        for ch in s1:
            s1_map[ch] = s1_map.get(ch, 0) + 1
        

        s2_map = {}
        for l, ch in enumerate(s2):
            if ch not in s1_map:
                continue

            s2_map[ch] = 1
            
            r = l + 1
            
            while r < len(s2) and s2[r] in s1_map:

                s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1

                if s1_map == s2_map:
                    return True

                if s2_map[s2[r]] > s1_map[s2[r]]:
                    # print("breaking")
                    break

                # print(s2_map, l)
                r += 1
                

            if s1_map == s2_map:
                return True
            s2_map = {}
            # print("new")

        return False