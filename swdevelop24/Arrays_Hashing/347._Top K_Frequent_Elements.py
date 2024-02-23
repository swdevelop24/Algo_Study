class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = dict()
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        arr = sorted(count, key=lambda x: count[x], reverse=True)
        return arr[:k]


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(sol.topKFrequent([1], 1))
