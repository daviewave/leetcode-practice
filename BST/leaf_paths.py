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

def leaf_paths(root):
    if not root:
        return None

    paths = []
    curr_path = ""
    def traverse(node):
        nonlocal paths
        nonlocal curr_path
        if not node:
            return

        prev_path = curr_path
        if not node.left and not node.right:
            curr_path = curr_path + f"{node.val}"
            paths.append(curr_path)
        else:
            curr_path = curr_path + f"{node.val}->"
        
        traverse(node.left)
        traverse(node.right)
        curr_path = prev_path
        
    traverse(root)
    return paths

if __name__ == "__main__":
    leaf_paths()