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
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            j += 1 # Increase for the #

            # Using the Length, get the string
            curr_str = s[j:j + length]
            decoded_list.append(curr_str)

            i = j + length

        return decoded_list