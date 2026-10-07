class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        last_start,last_end = intervals[0]

        for start,end in intervals:

            if start<=last_end:
                last_end = max(end,last_end)
            else:
                res.append([last_start,last_end])
                last_start,last_end=start,end
        
        res.append([last_start,last_end])
        return res