class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        print(string)
        left = 0
        right = len(string) - 1
        while left < right:
            # while string[left] == " " and left < right:
            #     left+=1
            # while string[right] == " " and left < right:
            #     right-=1

            if not string[left].isalnum():
                left += 1
                continue
            
            if not string[right].isalnum():
                right -= 1
                continue

            if string[left] != string[right]:
                print(left)
                print(right)
                return False

            left += 1
            right -= 1


        return True
        