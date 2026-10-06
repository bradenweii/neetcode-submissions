class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        s = sorted(nums)
        def dfs(start):
            res.append(subset[:])

            for i in range(start, len(nums)):
                # skip duplicates at the same recursion depth
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
        dfs(0)
        return res
