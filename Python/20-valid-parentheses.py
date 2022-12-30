class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["[", "{", "("]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif char == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                elif char == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif char == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False