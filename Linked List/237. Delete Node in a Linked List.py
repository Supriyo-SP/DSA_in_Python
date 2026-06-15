"""Delete a node from a linked list when only that node is given."""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next
                


        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """


if __name__ == "__main__":
    head = build_list([4, 5, 1, 9])
    node_to_delete = head.next
    Solution().deleteNode(node_to_delete)
    print(list_to_pylist(head))

    head = build_list([1, 2, 3, 4])
    node_to_delete = head.next.next
    Solution().deleteNode(node_to_delete)
    print(list_to_pylist(head))
        