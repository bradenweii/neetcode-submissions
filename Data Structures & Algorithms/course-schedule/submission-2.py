class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        vis = set()

        def dfs(course):
            if course in vis:
                return False
            vis.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            vis.remove(course)

            return True
        for i in range(numCourses):
            if not dfs(i): return False

        
        return True
