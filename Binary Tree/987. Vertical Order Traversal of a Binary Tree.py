# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q=deque([(root,0,0)])
        cols=defaultdict(list)
        min_col, max_col=0, 0
        while q:
            node, col, row= q.popleft()
            min_col, max_col = min(min_col,col),max(max_col,col)
            cols[col].append((row,node.val))
            if node.left:
                q.append((node.left, col - 1, row + 1))
            if node.right:
                q.append((node.right, col + 1, row + 1))
        return [[val for row, val in sorted(cols[c])] for c in range(min_col, max_col + 1)]        
            
        