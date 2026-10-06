class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        vis = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in vis or grid[r][c] == -1:
                return INF   
            if grid[r][c] == 0:
                return 0

            vis.add((r, c))
            best = 1 + min(
                dfs(r+1, c),
                dfs(r-1, c),
                dfs(r, c+1),
                dfs(r, c-1),
            )
            vis.remove((r, c))
            return best

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = dfs(r, c)





