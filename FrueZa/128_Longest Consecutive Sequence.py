class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        set_nums = set(nums)
        max_len = 1
        for num in set_nums:
            if num - 1 not in set_nums:
                curr_num = num
                count = 1
                while curr_num + 1 in set_nums:
                    count+=1
                    curr_num+=1
                max_len = max(max_len, count)

        return max_len

        