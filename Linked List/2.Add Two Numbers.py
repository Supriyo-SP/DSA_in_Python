# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        f=l1
        s=l2
        res1=0
        res2=0
        while f:
            d=f.val
            res1= res1 * 10 +d
            f=f.next    
        while s:
            res2 = res2 * 10+ s.val
            s=s.next
        reversed_num1= int(str(res1)[::-1])
        reversed_num2= int(str(res2)[::-1])
        while True:
            if not l1:
                break
            if l1.val==0:
                reversed_num1 *= 10
            else:
                break    
            l1=l1.next
        while True:
            if not l2:
                break
            if l2.val==0:
                reversed_num2 *= 10
            else:
                break
            l2=l2.next  
        result=reversed_num1 + reversed_num2
        # reverse_res=int(str(result)[::-1])
        dummy = ListNode(0)
        curr = dummy
        if result == 0:
            return ListNode(0)

        while result > 0:
            digit = result % 10
            curr.next = ListNode(digit)
            curr = curr.next
            result //= 10

        return dummy.next
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        