""" #Time Complexity -> O(n)
#Space Complexity -> O(n)
#Approach:
1. create 2 dictionaries to store key value pairs for both strings
2. check occurences for each string
3. check if dictionaries are equal and return the result
 """
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False


        dict_s = {}
        dict_t = {}

        # Count occurrences in string s
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1

        # Count occurrences in string t
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        return dict_s == dict_t