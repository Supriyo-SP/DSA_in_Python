 Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        nodes = []
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node.val)
                inorder(node.right)
        inorder(root)
        for i in range(1,len(nodes)):
            if nodes[i] <= nodes[i-1]:
                return False
        return True 