
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])

        q = deque()
        fresh=0
        min = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()

                for dr,dc in dir:
                    nr, nc = r + dr, c + dc

                    if(0<=nr<row and 0<=nc<col and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc))

            min+=1

        return min if fresh==0 else -1
            
        