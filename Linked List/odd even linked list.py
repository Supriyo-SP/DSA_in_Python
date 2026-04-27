# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        e=head.next
        o=head
        eh=e
        while e and e.next:
            o.next=o.next.next
            o=o.next
            e.next=e.next.next
            e=e.next
        o.next=eh
        return head    
        
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        