# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        def swap(node):
            if node is None:
                return
            node.left,node.right= node.right,node.left
            swap(node.left)
            swap(node.right)
        swap(root)
        return root    

        