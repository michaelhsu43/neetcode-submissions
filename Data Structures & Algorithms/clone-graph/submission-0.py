"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        return self.dfs(node)

    def dfs(self, node, clone_map={}) -> Optional['Node']:
        if node in clone_map:
            return clone_map[node]
        
        copied_node = Node(node.val)

        clone_map[node] = copied_node

        for neighbor in node.neighbors:
            copied_neighbor = self.dfs(neighbor, clone_map)
            copied_node.neighbors.append(copied_neighbor)
        
        return copied_node