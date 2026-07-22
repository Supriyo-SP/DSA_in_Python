# 104. Maximum Depth of Binary Tree
# Problem: return the number of nodes on the longest path from root to leaf.

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

        # Recursive DFS: depth of a node = 1 + max(depth of left, depth of right).
        def height(node):
            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)
            return 1 + max(left_height, right_height)

        return height(root)


# Better approach:
# - Level-order traversal (BFS) can also compute depth by counting levels.
# Time Complexity: O(n)
# Space Complexity: O(h) for recursion stack, where h is the tree height.