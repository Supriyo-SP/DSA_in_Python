"""Remove duplicate values from a sorted linked list."""


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
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        temp=head
        f=head.next
        while temp and f:
            if temp.val==f.val:
                temp.next=f.next
                f=f.next
            else:
                f=f.next
                temp=temp.next
        return head                            


if __name__ == "__main__":
    head = build_list([1, 1, 2, 3, 3])
    result = Solution().deleteDuplicates(head)
    print(list_to_pylist(result))

    head = build_list([1, 1, 1])
    result = Solution().deleteDuplicates(head)
    print(list_to_pylist(result))