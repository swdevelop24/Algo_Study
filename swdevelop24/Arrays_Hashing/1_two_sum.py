class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        start = 0
        last = len(nums)
        while True:
            for idx in range(start + 1, last):
                if nums[idx] == target - nums[start]:
                    return [start, idx]
            start += 1


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 2, 3], 6))
