class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        vis = set()
        q = deque()

        def bfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in vis or grid[r][c] == -1:
                return 
            vis.add((r,c))
            q.append([r,c])   

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    vis.add((r,c))
        dis = 0

        while q:
            
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dis
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)

            dis+=1


     