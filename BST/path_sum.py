# Time: O(n) -> depends on size of nums array passed in
# Space: O(h) -> since recursion creates a call stack O(h) is used where:
#                   - balanced tree == O(log n) 
#                   - skewed tree == O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sum(root, target_sum):
    from collections import deque
    if not root:
        return False

    queue = deque([(root, root.val)])
    while queue:
        node, curr_total = queue.popleft()
        if not node.left and not node.right:
            if curr_total == target_sum:
                return True

        if node.left:
            queue.append((node.left, curr_total + node.left.val))

        if node.right:
            queue.append((node.right, curr_total + node.right.val))

    return False

if __name__ == "__main__":
    path_sum()