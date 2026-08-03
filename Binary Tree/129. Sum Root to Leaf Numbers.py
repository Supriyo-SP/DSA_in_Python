# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        current = 0
        def sumRoot(node,current):
            if node is None:
                return 0
            current = (current *10) + node.val
            if not node.left and not node.right:
                return current
            left_sum = sumRoot(node.left, current)
            right_sum = sumRoot(node.right, current)
            
            return left_sum + right_sum
        return sumRoot(root,0) 