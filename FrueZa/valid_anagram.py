# Time Complexity: O(N)
# Space Complexity: O(N)
# Approach:
# 1. Create two dictionaries (s_freq and t_freq) to count the frequencies of characters in strings s and t.
# 2. Loop through string s and update s_freq with character frequencies.
# 3. Loop through string t and update t_freq with character frequencies.
# 4. If the lengths of the two dictionaries are not equal, return False, as the strings cannot be anagrams.
# 5. Compare the two dictionaries (s_freq and t_freq) to check if they are identical. If they are, return True; otherwise, return False.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}

        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        return s_freq == t_freq
