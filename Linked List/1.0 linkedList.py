"""Basic linked list node demo."""


class ListNode:
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


if __name__ == "__main__":
    node1 = ListNode(2)
    node2 = ListNode(4)
    node1.next = node2
    print(node1.next.val)
    print(node2.val)

    head = build_list([1, 2, 3])
    print(list_to_pylist(head))