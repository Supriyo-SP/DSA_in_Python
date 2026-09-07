# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = deque([root])
        result = []
        track = 0
        while queue:
            l = len(queue)
            output = []
            for _ in range(l):
                node = queue.popleft()
                output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if track % 2 != 0:
                output.reverse()
            result.append(output)
            track += 1
        return result 