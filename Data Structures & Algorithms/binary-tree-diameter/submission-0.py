# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global max_diameter
        max_diameter = 0

        self.dfs(root)

        return max_diameter

    def dfs(self, root:Optional[TreeNode]) -> int:
        global max_diameter
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        max_diameter = max(max_diameter, left + right)

        
        return 1 + max(left, right)

        



