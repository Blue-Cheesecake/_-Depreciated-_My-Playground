# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        prev = None
        current = head
        while current is not None:
            front = current.next
            current.next = prev
            prev = current
            current = front
        head = prev
        return head
