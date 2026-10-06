class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        vis = set()
        q = deque()
        if not grid:
            return 0


        def bfs(i,j):
            if i<0 or j<0 or i>=row or j>=col or (i,j) in vis or grid[i][j]!=1:
                return
            grid[i][j] = 2
            vis.add((i,j))
            q.append([i,j])


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i,j])
                    vis.add((i,j))
                
        minutes = -1

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            minutes+=1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return max(0,minutes)