class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ptr = 0
        while ptr < len(tokens):            
            if tokens[ptr] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[ptr] == "-":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(operand_1 - operand_2)
            elif tokens[ptr] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[ptr] == "/":
                operand_2 = stack.pop()
                operand_1 = stack.pop()                        
                stack.append(int(operand_1 / operand_2))
            else:
                stack.append(int(tokens[ptr]))
            ptr += 1
        return stack[0]