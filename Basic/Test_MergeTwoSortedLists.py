# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        main = l1
        another = l2

        if main is None:
            return l2
        elif another is None:
            return l1

        retL1 = True
        # check which one should be main node (ini with the lowest)
        if another.val < main.val:
            retL1 = False
            main = l2
            another = l1

        while main is not None or another is not None:
            if another is not None and main.next is not None:
                if another.val <= main.next.val:
                    temp = main.next
                    main.next = ListNode(another.val)
                    main.next.next = temp
                    another = another.next
                else:
                    main = main.next
            else:
                if main.next is None:
                    main.next = another
                    break
                elif another is None:
                    break

        if retL1:
            return l1
        else:
            return l2
