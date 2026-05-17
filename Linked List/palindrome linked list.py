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
    def isPalindrome(self, head):
        if head==None:
            return False
        s=[]
        temp=head
        while temp is not None:
            s.append(temp.val)
            temp=temp.next
        return s==s[::-1]           
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """


if __name__ == "__main__":
    head = build_list([1, 2, 2, 1])
    print(Solution().isPalindrome(head))
        