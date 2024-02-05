# Neetcode
"""
what is anagram?  made up of the exact list of characters
approach: count the occrances of the characters in both strings => hashmap

time: O(S+T)
space: O(S+T) => b/c we are building a hashmap 
downside: wea are building an extra memory

"""
# 1) hashmap solution


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            # key error will occur if wirtten like this
            # countS[s[i]] = 1 + countS[s[i]]
            # to avoid that => use get method with second parameter-> default value:0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True


print(Solution.isAnagram(Solution, "anagram", "nagaram"))

# 2) Counter library (not that recommended for an interview)
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


print(Solution.isAnagram(Solution, "anagram", "nagaram"))


# 3) sortecd order : time complexity => nlogn //
# space complexity : usually o(1) during the interview  you need to discuss
# not as efficent as the above two solutions
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


print(Solution.isAnagram(Solution, "anagram", "nagaram"))
