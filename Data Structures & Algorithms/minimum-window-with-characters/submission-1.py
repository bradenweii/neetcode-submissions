from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        arr = []
        t_count = Counter(t)  # Count of each character in t

        for i in range(len(s)):
            for j in range(i, len(s)):
                cur = s[i:j+1]
                cur_count = Counter(cur)

                # Check if cur satisfies t_count
                valid = True
                for char in t_count:
                    if cur_count[char] < t_count[char]:
                        valid = False
                        break

                if valid:
                    arr.append(cur)

        if not arr:
            return ""  # no substring found

        # Return the smallest valid substring
        arr.sort(key=len)
        return arr[0]
