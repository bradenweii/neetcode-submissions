class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[None] * n for _ in range(n)]      

        def calc(l,r):
            if dp[l][r] is not None:
                return dp[l][r]
            if l==r:
                return True
            if r-l==1:
                return s[l]==s[r]
            
            result = s[l] == s[r] and calc(l + 1, r - 1)
            dp[l][r] = result

            return result
                
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
        

            
            
            
        
        