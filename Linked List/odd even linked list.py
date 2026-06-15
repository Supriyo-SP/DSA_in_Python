"""Rearrange nodes so odd-indexed nodes come before even-indexed ones."""


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
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        e=head.next
        o=head
        eh=e
        while e and e.next:
            o.next=o.next.next
            o=o.next
            e.next=e.next.next
            e=e.next
        o.next=eh
        return head    
        
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    result = Solution().oddEvenList(head)
    print(list_to_pylist(result))

    head = build_list([2, 1, 3, 5, 6, 4, 7])
    result = Solution().oddEvenList(head)
    print(list_to_pylist(result))
        