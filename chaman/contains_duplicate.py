""" #Time Complexity -> O(n)
#Space Complexity -> O(n)
#Approach:
1. Create a Hashmap/Dictionary with key value pairs
2. Check for values having count more than 1 using Counter library
3. If any item has count > 1, then return True
4. Else, return False
 """
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}

        length = len(nums)

        for i in range(length):
            dictionary[i] = nums[i]

        
        count_dict = Counter(dictionary.values())
        
        for key, value in count_dict.items():
            if value > 1:
                return True
        
        return False