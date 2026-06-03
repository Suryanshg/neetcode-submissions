class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # Construct count map for s1
        s1_map = {}
        s2_map = {}
        for i in range(len(s1)):
            print(i)
            s1_map[s1[i]] = 1 + s1_map.get(s1[i], 0)
            s2_map[s2[i]] = 1 + s2_map.get(s2[i], 0)


        if s1_map == s2_map:
            return True


        # print(s2_map)

        l = 0
        for r in range(len(s1), len(s2)):
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]
            l += 1


            s2_map[s2[r]] = 1 + s2_map.get(s2[r], 0)
            
            print(s2_map)

            if s1_map == s2_map:
                return True

        


    
        # return False at the end
        return False
        