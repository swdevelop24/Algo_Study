'''
Time Complexity -> O(1)
#Space Complexity -> O(N)
#Approach:
1. Create a default dictionary and loop through each string and add entries accordinly  
2. if length of two arrays does not match, 
'''

from collections import defaultdict
class Solution(object):
      def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dats= defaultdict(int)
        datt= defaultdict(int)


        for x in s:
            dats[x]+=1
        for x in t:
            datt[x]+=1
        
        if len(dats) != len(datt):
            return False

        
        for x in dats:
            if dats[x]!= datt[x]:
                return False
            
        return True

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))