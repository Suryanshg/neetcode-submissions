class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if len(s) < len(t):
        #     return ""

        t_count = {}
        for ch in t:
            t_count[ch] = 1 + t_count.get(ch, 0)


        min_substr_len = float("infinity")
        min_substr = ""
        min_substr_map = {}
        
        l = 0
        for r in range(len(s)):
            min_substr_map[s[r]] = 1 + min_substr_map.get(s[r], 0)


            # check if t_count and min_substr_map has overlap
            overlap = True
            for ch in t_count.keys():
                if ch not in min_substr_map or t_count[ch] > min_substr_map[ch]:
                    overlap = False
                    break

            # print(f"r: {r} | overlap: {overlap} | map: {min_substr_map}")
            
            # while there is overlap
            while overlap:
                if r - l + 1 < min_substr_len:
                    min_substr_len = len(s[l : r + 1])
                    min_substr = s[l : r + 1]
                    # print(f"Found {min_substr}")

                min_substr_map[s[l]] -= 1
                l += 1

                for ch in t_count.keys():
                    if ch not in min_substr_map or t_count[ch] > min_substr_map[ch]:
                        overlap = False
                        break

                # print(f"r: {r} | overlap: {overlap} | map: {min_substr_map}")

                

        
        return min_substr
        