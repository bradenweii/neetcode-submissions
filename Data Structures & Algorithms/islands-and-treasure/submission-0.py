class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        EMPTY = 2147483647
        INF = 10**9

        def dfs(r, c, vis):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return INF
            if grid[r][c] == -1:
                return INF
            if (r, c) in vis:
                return INF
            if grid[r][c] == 0:
                return 0

            vis.add((r, c))
            best = 1 + min(
                dfs(r+1, c, vis),
                dfs(r-1, c, vis),
                dfs(r, c+1, vis),
                dfs(r, c-1, vis),
            )
            vis.remove((r, c))
            return best

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == EMPTY:
                    grid[r][c] = dfs(r, c, set())





