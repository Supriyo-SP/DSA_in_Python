# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ds=[]
        def rightview(node,level):  
            if node is None:
                return 
            if level== len(ds):
                ds.append(node.val)
            rightview(node.right,level+1)
            rightview(node.left,level+1)
        rightview(root,0)
        return ds