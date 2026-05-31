# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        # Example: Sort primarily by score descending, secondary by name alphabetically
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ptr = dummy
        heap = lists.copy()
        heapq.heapify(heap)
        while heap:
            node = heapq.heappop(heap)
            ptr.next = node
            ptr = ptr.next
            if node.next is not None:
                heapq.heappush(heap, node.next)



        return dummy.next