class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for s in stones:
            heapq.heappush(h,-s)
        
        while len(h)>1:
            x = -h[0]
            y = -h[1]
            if x!=y:
                y = abs(y-x)
                heapq.heappop(h)
                heapq.heappop(h)
                heapq.heappush(h,-y)
            else:
                heapq.heappop(h)
                heapq.heappop(h)

            print(h)
            
        return -h[0] if h else 0



        