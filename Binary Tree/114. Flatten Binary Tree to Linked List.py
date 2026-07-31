# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        temp_left = root.left
        temp_right = root.right
        root.left=None
        root.right=temp_left
        curr=root
        while curr.right:
            curr = curr.right
        curr.right = temp_right
        

        