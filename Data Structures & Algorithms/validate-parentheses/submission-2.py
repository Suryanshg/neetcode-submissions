class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(")")
            elif ch == "{": 
                stack.append("}")
            elif ch == "[":
                stack.append("]")
            else:
                if len(stack) > 0:
                    bracket = stack.pop(-1)
                    if bracket != ch:
                        return False
                else:
                    return False


        return len(stack) == 0