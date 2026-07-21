# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def height(node):
            if node==None:
                return 0
            leftheight=height(node.left)
            rightheight=height(node.right)
            m=max(leftheight,rightheight)
            return 1+m
        return height(root)        
#recursive approach   
# better solution will be level order     