class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            freq = [0]*26
            for c in word:
                freq[ord(c)-ord('a')]+=1
            map[tuple(freq)].append(word)
        return list(map.values())
        