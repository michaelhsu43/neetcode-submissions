# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        result = []

        tree = deque([root])

        while tree:
            level_size = len(tree)
            level_list = []
            for i in range(level_size):
                node = tree.popleft()
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
                level_list.append(node.val)
            
            result.append(level_list)
        
        return result
                