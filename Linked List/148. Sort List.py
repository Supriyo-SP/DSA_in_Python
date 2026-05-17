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
    def sortList(self, head):
        if head is None:
            return head
        temp=head
        li=[]
        while temp is not None:
            li.append(temp.val)
            temp=temp.next
        li.sort()
        temp=head
        i=0
        while temp is not None and i <len(li):
            temp.val=li[i]
            temp=temp.next
            i+=1
        return head    


        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


if __name__ == "__main__":
    head = build_list([4, 2, 1, 3])
    result = Solution().sortList(head)
    print(list_to_pylist(result))
        