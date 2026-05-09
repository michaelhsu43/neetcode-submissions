# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        dummyhead = ListNode(-1)
        dummyhead.next = head
        
        left = right = dummyhead
        for _ in range(n):
            right = right.next

        while right and right.next:
            left = left.next
            right = right.next

        left_next = left.next.next
        left.next = left_next

        return dummyhead.next