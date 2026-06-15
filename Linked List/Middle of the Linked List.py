"""Return the middle node of a linked list."""


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
class Solution(object):
    def middleNode(self, head):
        n=0
        temp=head
        while temp is not None:
            temp=temp.next
            n+=1
        temp=head
        for i in range(0,n//2):
            temp=temp.next
        return temp        
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    middle = Solution().middleNode(head)
    print(middle.val)

    head = build_list([1, 2, 3, 4, 5, 6])
    middle = Solution().middleNode(head)
    print(middle.val)
        