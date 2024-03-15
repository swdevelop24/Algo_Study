class Solution:
    def isPalindrome(self, s: str) -> bool:
        slist =[] 
        for ch in s:
            if ch >='A'and ch<='Z':
                ch = ch.lower()
                slist.append(ch)
            elif ch >='a' and ch <='z':
                slist.append(ch)
            elif ch >='0' and ch<='9':
                slist.append(ch)
            else: 
                continue
        
        length = len(slist)
        start =0
        end = length-1 

        if s == "":
            return True
        
        flag=0
        while(start < end):
            if (slist[start] == slist[end]):
                start+=1
                end-=1
            else:
                flag=1
                break
        
        if(flag):
            return False
        else: 
            return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))

