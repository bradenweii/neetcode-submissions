class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        count = 0
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        vis = set()

        def dfs(node):
            vis.add(node)
            for i in graph[node]:
                if i not in vis:
                    dfs(i)
        
        for i in range(n):
            if i not in vis:
                dfs(i)
                count+=1

        return count
        