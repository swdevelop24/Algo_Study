from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        ret_value = False

        length = len(nums)

        for i in range(length):
            dictionary[i] = nums[i]

        
        count_dict = Counter(dictionary.values())
        
        for key, value in count_dict.items():
            if value > 1:
                ret_value = True
        
        return ret_value