class Solution:
    def minWindow(self, s: str, t: str) -> str:
        arr = []
        for i in range(len(s)):
            for j in range(i,len(s)):
                cur = s[i:j+1]
                if set(t).issubset(set(cur)):
                    arr.append(cur)
        arr.sort(key=lambda x: len(x))
        return arr[0]


                    
                


        