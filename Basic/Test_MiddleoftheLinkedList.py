# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# bad solution


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # count how many node are there in linked list
        count = 0
        cur = head
        while cur is not None:
            count += 1
            cur = cur.next
        if count % 2 == 0:
            count /= 2
        else:
            count = count // 2
        count = int(count)
        hold = 0
        while hold < count:
            head = head.next
            hold += 1
        return head
