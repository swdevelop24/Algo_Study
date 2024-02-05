''' 
Time Complexity -> O(1)
#Space Complexity -> O(1) ?
#Approach:
1. Create a set from an existing list
2. Check if the the length of set and lists are the same
3. If different, duplicate number(s) exist(s) => returns true 
'''

class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums))!= len(nums)
    






