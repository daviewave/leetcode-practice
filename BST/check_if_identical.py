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

        
def check_if_identical(p, q):
    def are_identical(node1, node2):
        if not node1 and not node2:
            return True
        if (node1 and not node2) or (not node1 and node2):
            return False
        if node1.val != node2.val:
            return False
            
        if not are_identical(node1.left, node2.left):
            return False
        
        if not are_identical(node1.right, node2.right):
            return False
        
        return True

    return are_identical(p, q)

if __name__ == "__main__":
    function()