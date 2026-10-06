class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
        vis = set()
        def dfs(node):
            if node in vis:
                return False
            if graph[node]==[]:
                return True
            vis.add(node)
            for n in graph[node]:
                if not dfs(n):
                    return False
            #vis.remove(node)
            graph[node] = []
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        return True


   
        