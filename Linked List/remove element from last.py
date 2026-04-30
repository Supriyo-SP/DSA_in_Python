# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

