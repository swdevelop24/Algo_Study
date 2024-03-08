class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        cnt = 1
        ret = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == (nums[i - 1] + 1):
                    cnt += 1
                    ret = max(cnt, ret)
                else:
                    cnt = 1

        """    
        if len(nums) == 0:
            ret =0
        """

        if not nums:
            ret = 0

        return ret


sol = Solution()
print(sol.longestConsecutive([]))
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
