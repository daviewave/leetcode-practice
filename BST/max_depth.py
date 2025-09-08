# Time: O(n) -> depends on the amount of nodes in tree
# Space: O(h) -> since recursion creates a call stack O(h) is used where:
#                   - balanced tree == O(log n) 
#                   - skewed tree == O(n)
#-

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
        if not root:
            return 0
            
        def traverse(node, depth):
            if not node:
                return depth
            
            left = traverse(node.left, depth + 1)
            right = traverse(node.right, depth + 1)
            return max(left, right)
        
        return traverse(root, 0)

if __name__ == "__main__":
    max_depth()