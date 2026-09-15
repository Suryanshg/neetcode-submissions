class Solution:
    def calculate(self, s: str) -> int:
        stack = [] # Maintains operations for low precedence operators

        # Remove all whitespaces from s
        expr = "".join([c for c in s if c!=' '])

        # Variable to track the current num and prev operator
        num = 0
        previous_operator = '+' # default +


        for i in range(len(expr)):

            # If the character is a digit
            # Build the number
            if expr[i].isdigit():
                num = num * 10 + int(expr[i])

            
            # If the character is not a digit or if its the last character
            if (not expr[i].isdigit()) or i == len(expr) - 1:
                if previous_operator == '+':
                    stack.append(num)

                elif previous_operator == "-":
                    stack.append(-num)

                elif previous_operator == "*":
                    stack.append(stack.pop() * num)

                # Its division operator
                else:
                    stack.append(int(stack.pop() / num))

                # Update previous operator
                previous_operator = expr[i]

                # Reset current num
                num = 0

                
        print(stack)
        return sum(stack)