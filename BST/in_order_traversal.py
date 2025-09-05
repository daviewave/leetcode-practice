# Time: O(n) -> depends on the size of the BST passed in, will have to traverse the entire tree
# Space: O(n) -> creating a results list data structure to store values so the result list size depends on the size of the input BST
#-
# 
 
 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traversal(root):
    if not root:
        return []

    res = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        res.append(node.val)
        traverse(node.right)

    traverse(root)
    return res

if __name__ == "__main__":
    function()