# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        tree = deque([root])

        while tree:
            node = tree.popleft()
            if node.left:
                tree.append(node.left)
            if node.right:
                tree.append(node.right)
            
            
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True
        
        return False


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)