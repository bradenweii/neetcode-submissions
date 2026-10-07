class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(newInterval)
        intervals.sort()

        last_start, last_end = intervals[0]

        for start, end in intervals:
            if start <=last_end:
                last_end = max(last_end,end)
            else:
                res.append([last_start,last_end])
                last_start, last_end = start,end

        res.append([last_start,last_end])
        
        return res       


        