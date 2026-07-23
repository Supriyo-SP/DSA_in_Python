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
        pre=[]
        def preorder(node):
            if node ==None:
                return
            pre.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)    
        return pre  


        