# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        if not root:
            return []
        q.append(root)
        while q:
            qLen = len(q)
            print(qLen)
            level = []
           
            for _ in range(qLen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
                level.append(node.val)
            res.append(level[-1])
  
        return res
            