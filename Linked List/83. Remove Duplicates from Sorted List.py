# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        temp=head
        f=head.next
        while temp and f:
            if temp.val==f.val:
                temp.next=f.next
                f=f.next
            else:
                f=f.next
                temp=temp.next
        return head                            