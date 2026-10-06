class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        vis = set()
        row = len(heights)
        col = len(heights[0])
        pac,atl = False,False
        def dfs(i,j,val):
            nonlocal pac, atl
            if i<0 or j<0:
                pac = True
                return
            if i>=row or j>=col:
                atl = True
                return
            if heights[i][j]>val:
                return
            if pac and atl:
                return
            cur = heights[i][j]
            heights[i][j] = float('inf')
            dfs(i+1,j,cur)
            dfs(i-1,j,cur)
            dfs(i,j+1,cur)
            dfs(i,j-1,cur)
            heights[i][j] = cur

        res = []
        for r in range(row):
            for c in range(col):
                pac,atl = False,False
                dfs(r,c,float('inf'))
                if pac and atl:
                    res.append([r,c])
        return res

            
