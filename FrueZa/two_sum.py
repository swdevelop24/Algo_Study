class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary to store the numbers we've seen so far and their indices.
        seen = {}

        # Iterate over the list, with both the index and value of each item.
        for key, value in enumerate(nums):
            # Calculate the complement of the current value by subtracting it from the target.
            complement = target - value

            # Check if the complement exists in the dictionary (seen before).
            if complement in seen:
                # If found, return the indices of the complement and the current number.
                return [seen[complement], key]

            # If the complement is not found, add the current value and its index to the dictionary.
            seen[value] = key
