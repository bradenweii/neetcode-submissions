class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(stair):
            if stair <= 2:
                return stair
            if stair in memo:
                return memo[stair]
            memo[stair] = climb(stair-1)+climb(stair-2)
            return memo[stair]
        return climb(n)
        