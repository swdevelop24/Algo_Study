class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ret=[]
        for i, a in enumerate(nums):
            if i >0 and a == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1 
            while(left < right):
                sum = nums[i]+nums[left] + nums[right]
                if sum <0:
                    left+=1
                elif sum >0:
                    right -=1
                else:
                    temp = [nums[i], nums[left], nums[right]]
                    if temp not in ret:
                        ret.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[i] == nums[left]:
                        left+=1

        return ret

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]])
print(sol.threeSum([0,1,1])) # [] 
print(sol.threeSum([0,0,0])) # [[0,0,0]]
print(sol.threeSum([-1,0,1,0])) # [[-1,0,1],[-1,0,1]]
