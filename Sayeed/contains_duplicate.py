class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        # Approach:
        # 1. Initialize an empty set to keep track of seen numbers.
        # 2. Iterate over each number in the given list.
        #     a. Check if the current number is already in the set.
        #     b. If it is, return True as a duplicate is found.
        #     c. If not, add the number to the set.
        # 3. If no duplicates are found during iteration, return False.

        seen_set = set()
        for num in nums:
            if num in seen_set:
                return True
            seen_set.add(num)
        return False
