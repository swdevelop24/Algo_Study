# NEETCODE
"""
1) BRUTE FORCE : check one vs the next one : time - O(N^2), space - O(1)-no extra memory required
2) SORTING & Check adjacent values :  1 2 3 1 => 1 1 2 3 : time O(NlogN), space - O(1)
3) HASHSET: Does this exist in your hashset, if not add to the hashset? 1,2,3,1 
   time- O(N) & space O(N)
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False


sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))
print(Solution.containsDuplicate(Solution, [1, 2, 3, 4]))
