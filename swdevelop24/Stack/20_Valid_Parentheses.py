class Solution:
    def isValid(self, s: str) -> bool:
        stack =[] 
        for ch in s: 
            if ch == "(" or ch == "{" or ch == "[" :
                stack.append(ch)
            elif  ch == ")" or ch == "}" or ch == "]" :
                if not stack:
                    return False
                elif ch == ')' and stack[-1] =='(':
                    stack.pop() 
                elif ch == '}' and stack[-1] =='{':
                    stack.pop() 
                elif ch == ']' and stack[-1] =='[':
                    stack.pop()
                else:
                    break
        
        if not stack:
            return True
        else:
            return False   
        
sol=Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
