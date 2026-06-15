"""Detect whether a linked list contains a cycle."""


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

class Solution(object):
    def hasCycle(self, head):
        temp=head
        s=set()
        while temp is not None:
            if temp in s:
                return True
            else:
                s.add(temp)
                temp=temp.next
        return False            
        """
        :type head: ListNode
        :rtype: bool
        """


if __name__ == "__main__":
    head = build_list([3, 2, 0, -4])
    head.next.next.next.next = head.next
    print(Solution().hasCycle(head))

    head = build_list([1, 2, 3, 4])
    print(Solution().hasCycle(head))
        