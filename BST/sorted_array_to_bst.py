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


def sorted_array_to_bst_slow(nums):
        if not nums:
            return None

        mid = len(nums) // 2
        curr_root = TreeNode(val=nums[mid])
        curr_root.left = sorted_array_to_bst_slow(nums[:mid])
        curr_root.right = sorted_array_to_bst_slow(nums[mid+1:])
        return curr_root


def sorted_array_to_bst_fast(nums):
    def convert(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        new_node = TreeNode(val=nums[mid])
        new_node.left = convert(left, mid - 1)
        new_node.right = convert(mid + 1, right)
        return new_node
    return convert(0, len(nums) - 1)

if __name__ == "__main__":
    sorted_array_to_bst_fast([-10, -3, 0, 5, 9])