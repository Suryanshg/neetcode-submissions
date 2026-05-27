class Solution:

    def encode(self, strs: List[str]) -> str:
        full_encoded = ""
        for string in strs:
            encoded_str = str(len(string)) + "#" + string
            full_encoded += encoded_str
        return full_encoded


    def decode(self, s: str) -> List[str]:
        decoded_list = []        
        s_len = len(s)
        i = 0
        while i < s_len:
            j = i
            # Get the Length of the string
            curr_str_len = ""
            while s[j] != "#":
                curr_str_len += s[j]
                j += 1
            
            j += 1 # Increase for the #

            curr_str_len = int(curr_str_len)

            # Using the Length, get the string
            curr_str = s[j:j + curr_str_len]
            decoded_list.append(curr_str)

            i = j + curr_str_len

        return decoded_list