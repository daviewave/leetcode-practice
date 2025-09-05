# Time: O(n) -> depends on the size of p & q tree's passed in as args
# Space: O(h) -> since recursion creates a call stack O(h) is used where:
#                   - balanced tree == O(log n) 
#                   - skewed tree == O(n)
#-

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetrical(root):
    def is_mirrior(left_node, right_node):
        if not left_node and not right_node:
            return True
        if not left_node or not right_node:
            return False
        if left_node.val != right_node.val:
            return False

        return is_mirrior(left_node.left, right_node.right) and is_mirrior(left_node.right, right_node.left)
                
    if not root:
        return True
    return is_mirrior(root.left, root.right)

if __name__ == "__main__":
    function()