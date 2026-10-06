class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[b].append(a)
        vis = set()
        def dfs(course):
            if course in vis:
                return False
            if graph[course] == []:
                return True
            vis.add(course)
            for p in graph[course]:
                if not dfs(p): 
                    return False
            vis.remove(course)
            graph[course]= []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


    
    
            
        