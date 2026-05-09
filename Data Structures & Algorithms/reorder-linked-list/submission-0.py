# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> ListNode:
    
    prev = None
    cur = head

    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    return prev
        


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        second_half = reverseList(second)

        left, right = head, second_half

        while right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            right.next = tmp1

            left, right = tmp1, tmp2

        

        return
        