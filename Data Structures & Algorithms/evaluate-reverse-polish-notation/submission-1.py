class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for num in tokens:
            if num not in {"+", "-", "*", "/"}:
                stack.append(int(num))
            else:
                digit2 = stack.pop()
                digit1 = stack.pop()
                if num == "-":
                    stack.append(digit1 - digit2)
                elif num == "+":
                    stack.append(digit1 + digit2)
                elif num == "*":
                    stack.append(digit1 * digit2)
                else:
                    stack.append(int(digit1 / digit2))
                
        return stack[0]
