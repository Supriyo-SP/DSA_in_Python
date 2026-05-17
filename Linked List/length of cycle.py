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
	def lengthCycle(self, head):
		slow = head
		fast = head
		while fast is not None and fast.next is not None:
			slow = slow.next
			fast = fast.next.next
			if slow is fast:
				count = 1
				fast = fast.next
				while fast is not slow:
					count += 1
					fast = fast.next
				return count
		return 0


if __name__ == "__main__":
	head = build_list([1, 2, 3, 4, 5])
	head.next.next.next.next.next = head.next.next
	print(Solution().lengthCycle(head))
