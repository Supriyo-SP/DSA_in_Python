"""Reorder a linked list by alternating nodes from the front and back."""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def list_to_pylist(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        curr=second
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        second=prev
        first=head
        while second:
            temp_f=first.next
            temp_s=second.next
            first.next=second
            second.next=temp_f
            first=temp_f
            second=temp_s


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4])
    Solution().reorderList(head)
    print(list_to_pylist(head))

    head = build_list([1, 2, 3, 4, 5])
    Solution().reorderList(head)
    print(list_to_pylist(head))

