"""Remove the n-th node from the end of a linked list."""


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
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head
        if head.next is None and n==1:
            return None    
        temp=head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        if count==n:
            newhead=head.next
            del head
            return newhead    
        temp=head    
        d=count-n
        c=1
        while temp is not None and temp.next is not None:
            if c==d:
                temp.next=temp.next.next
            temp=temp.next
            c+=1  
        return head      
            
            

        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
#optimal:


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(head, 2)
    print(list_to_pylist(result))

    head = build_list([1, 2])
    result = Solution().removeNthFromEnd(head, 2)
    print(list_to_pylist(result))

