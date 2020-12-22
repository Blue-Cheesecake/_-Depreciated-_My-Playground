class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # ! Init --> check if the next is similar or not
        main = head

        if main is not None or main.next is None:
            return head

        while main is not None:
            data = main.val
            rev = False
            if main.next is not None:
                # ? if data main == data the next --> remove
                if data == main.next.val:
                    main.next = main.next.next
                    rev = True

            if not rev:
                main = main.next

        return main
