class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for w in words for c in w}
        dics = set(''.join(words))
  
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        res={}
        vis = set()
        res = []
        vis, cycle = set(),set()
        def dfs(c):
            if c in vis:
                return True
            #cycle.add(c)
            for n in graph[c]:
                if not dfs(n): return False
            #cycle.remove(c)
            vis.add(c)
            res.append(c)
            return True

        for c in dics:
            if not dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)


         