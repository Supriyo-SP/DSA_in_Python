# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def max_width(node):
            q = deque([(node,0)])
            m_width = 0
            while len(q)>0:
                current_size = len(q)
                start = q[0][1]
                end = q[-1][1]
                m_width=max(m_width,(end-start)+1)
                for i in range (current_size):
                    node,val = q.popleft()
                    if node.left:
                        q.append((node.left, val*2 + 1))
                    if node.right:
                        q.append((node.right, val*2 + 2)) 
            return m_width
        return max_width(root)
#preety hard to solve
