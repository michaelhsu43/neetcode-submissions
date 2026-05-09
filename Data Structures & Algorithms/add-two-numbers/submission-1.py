# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1, num_2 = 0, 0

        digits = 1
        while l1:
            num_1 += digits * l1.val
            digits *= 10
            l1 = l1.next

        digits = 1
        while l2:
            num_2 += digits * l2.val
            digits *= 10
            l2 = l2.next
            
        answer = num_1 + num_2
        if answer == 0:
            return ListNode(0)
        
        dummy = ListNode(0)
        cur = dummy
        while answer != 0:
            answer, remainder = divmod(answer, 10)
            cur.next = ListNode(remainder)
            cur = cur.next

        return dummy.next




        