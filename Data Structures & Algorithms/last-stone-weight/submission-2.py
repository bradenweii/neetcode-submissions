class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for s in stones:
            heapq.heappush(h,-s)
        
        while len(h)>1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(y)

            if x!=y:
                heapq.heappush(h,-(x - y))
            

        return -h[0] if h else 0



        