"""Delete the middle node from a singly linked list."""


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
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        slow=head
        fast=head
        fast=head.next.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head


if __name__ == "__main__":
    head = build_list([1, 3, 4, 7, 1, 2, 6])
    result = Solution().deleteMiddle(head)
    print(list_to_pylist(result))

    head = build_list([1, 2, 3, 4])
    result = Solution().deleteMiddle(head)
    print(list_to_pylist(result))