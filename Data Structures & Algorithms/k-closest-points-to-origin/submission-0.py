class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        for i,(x,y) in enumerate(points):
            dis = math.sqrt(x**2+y**2)
            points[i].append(dis)

        points.sort(key=lambda x:x[2])
        print(points)
        res=[]

        for a,b,c in points:
            if len(res)<k:
                res.append([a,b])

        return res

