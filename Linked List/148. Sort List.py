# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        