class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]      

        def calc(l,r):
            if (l,r) in memo:
                return memo[(l,r)]
            if l==r:
                return True
            if r-l==1:
                return s[l]==s[r]
            
            memo[(l,r)] = s[l]==s[r]
            return s[l]==s[r] and calc(l+1,r-1)
        
        best_l = 0
        best_r = 0
        memo = {}
        for l in range(n):
            for r in range(l, n):
                if calc(l, r):
                    if r - l > best_r - best_l:
                        best_l = l
                        best_r = r
        
        return s[best_l:best_r+1]
        

            
            
            
        
        