class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr.append(matrix[i][j])
        l,r = 0,len(arr)-1
        while l<=r:
            m = (l+r)//2
            if target == arr[m]:
                return True
            if arr[m]<target:
                l=m+1
            else:
                r = m-1
        return False
        