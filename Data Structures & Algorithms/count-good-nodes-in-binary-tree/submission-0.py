# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node,cur):
            nonlocal count
            if not node:
                return
            cur = max(cur,node.val)
            if cur == node.val:
                count+=1
            dfs(node.left,cur)
            dfs(node.right,cur)

        dfs(root,root.val)
        return count