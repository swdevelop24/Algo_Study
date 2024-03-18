class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = []
        i = 0
        for i in range(0, len(nums)):
            left_prod = 1
            right_prod = 1

            for j in range(0, i):
                left_prod *= nums[j]

            for j in range(i + 1, len(nums)):
                right_prod *= nums[j]

            prod_list.append(left_prod * right_prod)
        return prod_list



