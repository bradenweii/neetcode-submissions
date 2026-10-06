class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        vis = set()
        def dfs(node,parent):
            if node in vis:
                return False
            vis.add(node)
            for n in graph[node]:
                if n == parent:
                    continue
                if not dfs(node,parent):
                    return False
            return True
        
        return dfs(0,-1) and len(vis)==n



        