class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        dics = set(''.join(words))
  
        for i in range(len(words) - 1):
            for c1, c2 in zip(words[i], words[i+1]):
                if c1!=c2:
                    graph[c1].append(c2)
                    break
        res={}
        vis = set()
        res = []
        vis, cycle = set(),set()
        def dfs(c):
            if c in cycle:
                return False
            if c in vis:
                return True
            cycle.add(c)
            for n in graph[c]:
                if not dfs(n): return False
            cycle.remove(c)
            vis.add(c)
            res.append(c)
            return True

        for c in dics:
            if not dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)


         