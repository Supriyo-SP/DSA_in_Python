"""Rotate a linked list to the right by k places."""


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
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if k==0 or head is None or head.next is None:
            return head
        len=1
        tail=head
        while tail.next:
            tail=tail.next
            len+=1
        k=k%len   
        if k==0 :
            return head
        temp=head
        tail.next=head
        newtail=len-k-1
        for _ in range(newtail):
            temp=temp.next
        nhead=temp.next
        temp.next=None
        return nhead    


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    result = Solution().rotateRight(head, 2)
    print(list_to_pylist(result))

    head = build_list([0, 1, 2])
    result = Solution().rotateRight(head, 4)
    print(list_to_pylist(result))


