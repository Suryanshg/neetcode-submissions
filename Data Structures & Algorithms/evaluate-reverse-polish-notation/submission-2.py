class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_set = {"+", "-", "*", "/"}
        stack = []
        ptr = 0
        while ptr < len(tokens):
            if tokens[ptr] not in operation_set:
                stack.append(int(tokens[ptr]))
            else:
                operation = tokens[ptr]
                
                if operation == "+":
                    stack.append(stack.pop() + stack.pop())
                elif operation == "-":
                    operand_2 = stack.pop()
                    operand_1 = stack.pop()
                    stack.append(operand_1 - operand_2)
                elif operation == "*":
                    stack.append(stack.pop() * stack.pop())
                elif operation == "/":
                    operand_2 = stack.pop()
                    operand_1 = stack.pop()                        
                    stack.append(int(operand_1 / operand_2))
            ptr += 1
        return stack[0]