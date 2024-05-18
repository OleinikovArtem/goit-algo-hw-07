class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_max_value(root):
    if root is None:
        raise ValueError("The tree is empty")

    current = root
    while current.right is not None:
        current = current.right

    return current.value


def find_min_value(root):
    if root is None:
        raise ValueError("The tree is empty")

    current = root
    while current.left is not None:
        current = current.left

    return current.value


def sum_tree_values(root):
    if root is None:
        return 0

    left_sum = sum_tree_values(root.left)
    right_sum = sum_tree_values(root.right)

    return root.value + left_sum + right_sum


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(25)
    print('max_value:', find_max_value(root))  # Should print 25
    print('min_value:', find_min_value(root))  # Should print 5
    print('sum_tree_values:', sum_tree_values(root))  # Should print 75
