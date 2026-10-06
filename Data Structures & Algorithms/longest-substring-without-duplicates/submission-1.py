class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = set()
        i = 0
        ans = 0
        for j in range(len(s)):
            while s[j] in map:
                map.remove(s[i])
                i+=1
            map.add(s[j])
            ans = max(ans,j-i+1)
        return ans
        