# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        tree = deque([root])

        while tree:
            level_size = len(tree)
            for i in range(level_size):
                node = tree.popleft()
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
                
                if i == level_size - 1:
                    result.append(node.val)
        
        return result

