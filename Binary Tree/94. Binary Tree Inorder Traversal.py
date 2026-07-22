# 94. Binary Tree Inorder Traversal
# Problem: return the inorder traversal of a binary tree in left-root-right order.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        stack = []
        inorder = []
        node = root

        # Go left as far as possible, then visit nodes and move right.
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                inorder.append(node.val)
                node = node.right

        return inorder
        
#problem 1 

