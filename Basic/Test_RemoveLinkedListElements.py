# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = head
        if cur is None:
            return cur
        elif cur.next is None:
            if cur.val == val:
                head = None
            return head
        while cur is not None:
            stop = False
            if head.val == val:
                head = cur.next
            else:
                if cur.next is not None:
                    if cur.next.val == val:
                        cur.next = cur.next.next
                        stop = True
            if not stop:
                cur = cur.next
        return head
