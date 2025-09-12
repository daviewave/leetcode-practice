# Time: O(n) -> depends on the amount of nodes in tree
# Space: O(h) -> since recursion creates a call stack O(h) is used where:
#                   - balanced tree == O(log n) 
#                   - skewed tree == O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if not root:
        return root

    def invert(node):
        if not node:
            return None

        if not invert(node.left) and not invert(node.right):
            curr_left, curr_right = node.left, node.right
            node.left = curr_right
            node.right = curr_left

    invert(root)
    return root

if __name__ == "__main__":
    invert_tree()