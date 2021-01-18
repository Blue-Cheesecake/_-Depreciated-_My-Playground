package Basic;

// * Definition for singly-linked list.

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class RemoveLinkedListElements {

    public ListNode removeElements(ListNode head, int val) {

        ListNode cur = head;

        while (cur != null) {

            // ! incase index = 0
            if (cur.val == val) {
                head = head.next;
                cur = head;
                continue;
            }

            if (cur.next != null) {
                if (cur.next.val == val) {
                    cur.next = cur.next.next;
                    continue;
                }
            }

            cur = cur.next;
        }

        return head;
    }
}
