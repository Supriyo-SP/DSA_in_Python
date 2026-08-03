# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi = float("-inf")
        def dfs(node):
            if node is None:
                return 0
            leftsum = dfs(node.left)
            if leftsum < 0:
                leftsum=0
            rightsum = dfs(node.right)
            if rightsum < 0:
                rightsum=0
            self.maxi = max(self.maxi, leftsum+node.val+rightsum)
            return node.val+max(leftsum, rightsum)
        dfs(root)
        return self.maxi
# hard 

        