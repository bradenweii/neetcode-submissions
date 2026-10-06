class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            graph[u].append(v)
        res = []
        visit,cycle = set(),set()

        def dfs(node):
            if node in visit:
                return True
            if node in cycle:
                return False
            cycle.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return res


        