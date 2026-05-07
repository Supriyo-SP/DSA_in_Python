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
    def removeElements(self, head, val):
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while temp.next is not None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next


if __name__ == "__main__":
    head = build_list([1, 2, 6, 3, 4, 5, 6])
    val = 6
    result = Solution().removeElements(head, val)
    print(list_to_pylist(result))
        