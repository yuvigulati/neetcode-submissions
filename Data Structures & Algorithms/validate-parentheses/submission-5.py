class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for letter in s:
            if letter in pairs.values():
                stack.append(letter)
            elif letter in pairs:
                if not stack or stack[-1] != pairs[letter]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack



