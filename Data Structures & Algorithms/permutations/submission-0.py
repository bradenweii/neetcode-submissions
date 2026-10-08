class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        vis = [False]*n
        def bt(arr):
            if len(arr)==n:
                res.append(arr[:])
                return
        
            for i in range(n):
                if not vis[i]:
                    arr.append(nums[i])
                    vis[i]=True
                    bt(arr)

                    arr.pop()
                    vis[i]=False
        bt([])
        return res

        
