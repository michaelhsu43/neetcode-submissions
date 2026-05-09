"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None

        orig = head
        copy_head  = Node(-1)
        copy = copy_head
        orig_copy_map = dict()


        while orig and orig.next:
            copy.val = orig.val
            orig_copy_map[orig] = copy
            copy.random = orig.random
            
            copy.next = Node(-1)
            copy = copy.next
            orig = orig.next

        
        copy.val = orig.val
        orig_copy_map[orig] = copy
        copy.random = orig.random

        copy = copy_head

        while copy:
            copy_random = copy.random
            if copy_random != None:
                copy.random = orig_copy_map[copy_random]
    
            copy = copy.next
        return copy_head