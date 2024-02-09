class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        map = {}

        for s in strs:
            key = str(sorted(s))
            if key not in map:
                map[key] = []
            map[key].append(s)
        return list(map.values())


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))
