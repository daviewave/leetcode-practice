# Time: O(n) -> depends on the amount of nodes in tree
# Space: O(h) -> since recursion creates a call stack O(h) is used where:
#                   - balanced tree == O(log n) 
#                   - skewed tree == O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def traverse(node):
        if not node:
            return 0
        
        left = traverse(node.left)
        if left == -1:
            return -1
        
        right = traverse(node.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)

    return traverse(root) != -1

if __name__ == "__main__":
    function()