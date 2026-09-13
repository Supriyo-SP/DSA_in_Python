# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev = None
        self.min_diff = float("inf")
        def dfs(node):
            if node is None:
                return 
            dfs(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff,node.val-self.prev)
            self.prev = node.val
            dfs(node.right)
        dfs(root)
        return self.min_diff