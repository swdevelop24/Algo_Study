class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top == '(' and bracket != ')':
                    return False
                if top == '{' and bracket != '}':
                    return False
                if top == '[' and bracket != ']':
                    return False
        return not stack
