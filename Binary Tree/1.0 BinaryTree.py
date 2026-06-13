class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def print_tree(root, prefix="", is_left=True):
    if root is None:
        return

    if root.right:
        new_prefix = prefix + ("|   " if is_left else "    ")
        print_tree(root.right, new_prefix, False)

    print(prefix + ("|-- " if is_left else "\\-- ") + str(root.val))

    if root.left:
        new_prefix = prefix + ("    " if is_left else "|   ")
        print_tree(root.left, new_prefix, True)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)

    print_tree(root)