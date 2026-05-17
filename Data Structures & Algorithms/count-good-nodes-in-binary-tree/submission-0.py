# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.dfs(root, root.val)

    def dfs(self, root:TreeNode, max_val: int) -> int:

        if not root:
            return 0
        
        cur = 0 if max_val > root.val else 1
        max_val = max(max_val, root.val)
        
        

        return self.dfs(root.left, max_val) + self.dfs(root.right, max_val) + cur

        