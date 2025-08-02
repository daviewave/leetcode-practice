# Time: O(n log n) -> .sort() ruins runtime efficiency
# Space: (1) -> dont have to create another data structure to help efficiency
#-
# in a sorted array can just maje sure the next is not == the current
def contains_duplicates_memory_efficient(nums):
    nums.sort()
    i = 0
    for j in range(1, len(nums)):
        if nums[i] == nums[j]:
            return True
        i += 1
        j += 1
    return False

# Time: O(n) -> only 1 loop so just depends on input size
# Space: O(n) -> creates a set that will have an unknown size 
#-
# use a set which has has O(n) seach for 'in' as a list of seen
def contains_duplicates_runtime_efficient():
    pass

if __name__ == "__main__":
    function()