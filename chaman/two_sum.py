""" #Time Complexity -> O(n)
#Space Complexity -> O(n)
# Approach:
# 1. Create a Hashmap/Dictionary to store the indices of previously seen numbers along with their values.
# 2. Iterate through the list, and for each number:
#    - Calculate the difference between the target and the current number.
#    - Check if this difference exists in the hashmap.
#    - If found, return the indices of the two numbers.
# 3. If no such pair is found, return an empty list.
 """
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i
        return