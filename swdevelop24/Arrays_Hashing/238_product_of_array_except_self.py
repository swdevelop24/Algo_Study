"""
class Solution:
    def produtExceptSelf(self, nums: list[int]) -> list[int]:
        ret = []
        cal = 1
        for i in range(len(nums)):
            j = 0
            while j < len(nums):
                if j == i:
                    j += 1
                    continue
                cal *= nums[j]
                j += 1
            ret.append(cal)
            cal = 1
        return ret


sol = Solution()
print(sol.produtExceptSelf([1, 2, 3, 4]))
print(sol.produtExceptSelf([-1, 1, 0, -3, 3]))
"""

# time limit error


# different approach
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = 1
        postfix = 1
        output = [0] * n
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        for i in range(n - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
print(sol.productExceptSelf([-1, 1, 0, -3, 3]))
