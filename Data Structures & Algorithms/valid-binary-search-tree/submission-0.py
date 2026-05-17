# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left = -float("inf")
        right = float("inf")

        return self.withinRange(root, left, right)
    def withinRange(self, root: Optional[TreeNode], left_range: int, right_range: int) -> bool:

        if not root:
            return True

        if not(root.val > left_range and root.val < right_range):
            return False

        return self.withinRange(root.left, left_range, root.val) and self.withinRange(root.right, root.val, right_range)