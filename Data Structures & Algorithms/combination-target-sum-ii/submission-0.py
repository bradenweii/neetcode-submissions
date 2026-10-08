class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        n = len(candidates)

        def back(i,total,arr):
            if total==target:
                res.append(arr[:])
                return
            
            for j in range(i,n):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if total+candidates[j]>target:
                    break
                
                arr.append(candidates[j])

                back(j+1,total+candidates[j],arr)

                arr.pop()

        back(0,0,[])
        return res


                
        

