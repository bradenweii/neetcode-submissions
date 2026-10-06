class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def add(self, word: str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    def __str__(self, level=0):
        children_str = ', '.join(f"{k}: {v.__str__(level+1)}" for k, v in self.children.items())
        indent = '  ' * level
        return f"\n{indent}TrieNode(is_end={self.end}, children={{ {children_str} }})"

    __repr__ = __str__


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add(word)
        row,col = len(board),len(board[0])
        res,visit =set(),set()

        def dfs(r,c,node,word):
            if (r<0 or c<0 or r==row or c==col 
            or (r,c) in visit or 
            board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            visit.remove((r,c))
        for r in range(row):
            for c in range(col):
                dfs(r,c,root,"")
        return list(res)
