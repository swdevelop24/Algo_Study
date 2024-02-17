class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict with list type to gather anagrams together.
        seen = defaultdict(list)

        # Iterate over each string in the provided list.
        for string in strs:
            # Sort the characters of the string and convert it to a tuple to use as a dictionary key.
            sort_str = tuple(sorted(string))
            # Debugging print statement to observe the sorted tuples.
            print(sort_str)
            # Append the original string into the list of its sorted character tuple key.
            seen[sort_str].append(string)

        # Convert the defaultdict values to a list and return. This groups all anagrams together.
        return list(seen.values())
