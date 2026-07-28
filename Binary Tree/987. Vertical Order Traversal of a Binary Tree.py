from collections import defaultdict, deque

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
        # Vertical order traversal rules:
        # 1. Nodes are grouped by their column index.
        # 2. Columns are returned from left to right.
        # 3. Inside one column, nodes are ordered by row from top to bottom.
        # 4. If two nodes share the same row and column, smaller value comes first.

        if root is None:
            return []

        # BFS gives us the row for free by level progression.
        queue = deque([(root, 0, 0)])
        columns = defaultdict(list)
        min_col = 0
        max_col = 0

        while queue:
            node, col, row = queue.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            # Store row and value so we can sort later with the exact problem rules.
            columns[col].append((row, node.val))

            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))

        answer = []
        for col in range(min_col, max_col + 1):
            current_column = sorted(columns[col])
            answer.append([value for row, value in current_column])

        return answer


# Approach summary:
# - Do a BFS while tagging every node with (column, row).
# - Group nodes by column in a hashmap.
# - Sort each column by (row, value).
# - Read columns from leftmost to rightmost.
# Time complexity: O(n log n) because of sorting.
# Space complexity: O(n) for the queue and the grouped nodes.
            
        