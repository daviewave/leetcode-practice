# Time: O(n)
# Space: O(1)
#-

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes(root):
    if not root: 
        return 0
    
    total = 0
    def traverse(node):
        if not node:
            return
        nonlocal total
        total += 1
        traverse(node.left)
        traverse(node.right)
    traverse(root)
    return total

if __name__ == "__main__":
    count_nodes()