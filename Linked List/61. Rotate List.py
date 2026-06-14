# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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


        