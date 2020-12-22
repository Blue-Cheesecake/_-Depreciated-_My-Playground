# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1211/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        # use Two pointers
        # slow one and fast one
        while fast is not None:
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return False
            if slow == fast:
                return True
        return False
