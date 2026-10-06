class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def count(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i]+count(i+2),count(i+1))
            return memo[i]
        return count(0)


                