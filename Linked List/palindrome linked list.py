# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        