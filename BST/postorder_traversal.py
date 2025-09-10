# Time: O(n) -> depends on size of nums array passed in
# Space: O(h) -> since recursion creates a call stack O(h) is used where:
#                   - balanced tree == O(log n) 
#                   - skewed tree == O(n)
#-

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root):
    if not root:
        return []

    res = []
    def traverse(node):
        if not node:
            return

        traverse(node.left)
        traverse(node.right)
        res.append(node.val)
    traverse(root)
    return res

if __name__ == "__main__":
    postorder_traversal()