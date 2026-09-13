class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        result = []
        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            result.append(node.val)
            traversal(node.right)
        traversal(root)
        result.sort()
        return result[k-1]