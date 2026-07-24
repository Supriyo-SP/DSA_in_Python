# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Preorder DFS order: Root -> Left -> Right.
        # This recursive solution is optimal for clarity.
        # Time complexity: O(n), each node is visited once.
        # Space complexity: O(h), recursion stack where h = tree height
        # (worst case O(n), balanced tree O(log n)).
        result = []

        def preorder(node):
            # Use `is None` for identity-based None checking in Python.
            if node is None:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        # Alternatives for future reference:
        # 1) Iterative preorder using an explicit stack.
        # 2) Morris preorder traversal for O(1) extra space.
        return result


        