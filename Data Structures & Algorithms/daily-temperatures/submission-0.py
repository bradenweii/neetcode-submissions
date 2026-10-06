class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures),-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if len(stack)==0:
                res[i]=0
            


        