import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v,w))
        
        heap = [(0,k)]
        vis={}
        while heap:
            time,node = heapq.heappop(heap)

            if node in vis:
                continue
            vis[node] = time

            for nei,w in adj[node]:
                if nei not in vis:
                    heapq.heappush(heap,(time+w,nei))
            
        if len(vis)!=n:
            return -1
            
        return max(vis.values())





