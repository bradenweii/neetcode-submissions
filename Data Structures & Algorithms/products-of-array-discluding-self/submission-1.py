class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        cur = 1
        for i in range(1,len(nums)):
            #ans[1] = ans[1]*nums[0] = 1*1
            #ans[2] = ans[2]*nums[1]*nums[0] = 
            #[1,1,1,1]
            #[1,2,3,4]
            #[1,1,2,6]
            cur *= nums[i-1]
            ans[i] = ans[i]*cur
        cur2=1
        for i in range(len(nums)-1,-1,-1):
            #ans[0] = ans[0]*nums[3]*nums[2]*nums[1]
            #ans[1] = ans[1]*nums[2]*nums[1]
            #ans[3] = ans[3]*
            ans[i] = ans[i]*cur2
            cur2 *= nums[i]
            
        return ans
        
        