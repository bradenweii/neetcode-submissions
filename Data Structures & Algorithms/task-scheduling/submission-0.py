class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = []
        count = Counter(tasks)
        for val in count.values():
            heapq.heappush(h,-1*val)

        q = deque()
        time = 0

        while h or q:
            time+=1

            if not h:
                time = q[0][1]
            else:
                cnt = 1+heapq.heappop(h)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(h,q.popleft()[0])

        return time



      

        