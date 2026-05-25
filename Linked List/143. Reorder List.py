# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        curr=second
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        second=prev
        first=head
        while second:
            temp_f=first.next
            temp_s=second.next
            first.next=second
            second.next=temp_f
            first=temp_f
            second=temp_s

        